<template>
  <div class="wrap">

    <h1>信号一覧</h1>

    <div class="table-custom-util">
      <input type="text" v-model="searchValue" placeholder="SEARCH" />
    </div>
    <a @click="update()">最新の情報に更新する</a>
    <EasyDataTable
      show-index
      v-model:items-selected="itemsSelected"
      buttons-pagination
      :headers="headers"
      :items="items"
      :loading="loading"
      :rows-per-page="10"
      :search-field="searchField"
      :search-value="searchValue"
      alternating
    >
      <template #item-key="{ key }">
        <a @click="sendIR(key)">{{ key }}</a>
      </template>

      <template #item-operation="item">
        <div class="operation-wrapper">
          <div><a @click="editItem(item)">編集</a></div>
          <div><a @click="deleteItem(item)">削除</a></div>
        </div>
      </template>

      <template #expand="item">
        <div class="memo">
          <div>
            <span class="bold">value ({{ item.value.length }}): </span>
            <div class="signal">
              <span class="signal_item" v-for="(sig, i) in item.value" v-bind:key="i">{{ sig }}</span>
            </div>
          </div>
        </div>
        
      </template>
    </EasyDataTable>

    <a @click="deleteMulti()" v-if="itemsSelected.length">{{ itemsSelected.length }} 件のアイテムを削除</a>

    <div v-if="create_visible" class="darkbox">
      <h3>Creating "<pre class="inline">{{ newItem.key }}</pre>":</h3>
      <div>
        <div>key :<Multiselect
          v-model="newItem._key"
          :options="getList(newItem._key)"
          mode="tags"
        /></div>
        <div>desc:<input type="text" v-model="newItem.desc" /></div>
      </div>
      <div class="btns">
        <button @click="_save()">Save</button>
        <button @click="close_save()">Cancel</button>
      </div>
    </div>

    <div v-if="edit_visible" class="darkbox">
      <h3>Editing "<pre class="inline">{{ editingItem.key }}</pre>":</h3>
      <div>
        <div>desc:<input type="text" v-model="editingItem.desc" /></div>
      </div>
      <div class="btns">
        <button @click="_edit()">Save</button>
        <button @click="close_edit()">Cancel</button>
      </div>
    </div>

    <div v-if="delete_visible" class="darkbox">
      <h3>Delete "{{ deletingItem.key }}"?</h3>
      <div class="btns">
        <button @click="_delete()">Delete</button>
        <button @click="close_delete()">Cancel</button>
      </div>
    </div>

  </div>
</template>

<script setup>
import { ref, reactive } from "vue";
import Multiselect from '@vueform/multiselect';
// defineProps(/*{msg: String}*/)
const headers = [
  { text: 'key', value: 'key', sortable: true },
  { text: 'desc', value: 'desc', sortable: true },
  { text: '_', value: 'operation' }
]
const itemsSelected = ref([]);
const items = ref([]);

let dict = {};

const loading = ref(false);

const searchField = ref('key')
const searchValue = ref('');

const create_visible = ref(false);
const edit_visible = ref(false);
const delete_visible = ref(false);

/*type IRItem = {
  value: number[],
  desc : string
};
type IRItemTable = { [name: string]: IRItem };*/
const update = async () => {
  loading.value = true;
  const req = await fetch('/api/ir');
  if (req.status != 200) {
    return false;
  }
  const json = await req.json();
  items.value = Object.keys(json).map((v) => {
    return { key: v, ...json[v] }
  });
  loading.value = false;

  dict = {};
  for(const name of Object.keys(json)) {
    let tgt = dict;
    for(const n of name.split(':')) {
        tgt[n] = tgt[n] || {};
        tgt = tgt[n];
    }
  }
  return true;
}

const getList = names => {
    let tgt = dict;
    for(const n of names) {
        if (!(tgt = tgt?.[n])) return [];
    }
    return Object.keys(tgt);
}

// getList(['NEC', 'CEILING_LIGHT', 'a']);

const close_save = () => {
  create_visible.value = false;
}
const close_edit = () => {
  edit_visible.value = false;
}
const close_delete = () => {
  delete_visible.value = false;
}

const sendIR = async (key) => {
  loading.value = true;
  const req = await fetch(`/api/ir/${key}`);
  if (req.status != 200) {
    alert('Communication failed.');
    return false;
  }
  loading.value = false;
}

const newItem = reactive({
  _key: [],
  desc: ''
});
const _save = async () => {
  const { _key, desc } = newItem;
  const key = _key.join(':');
  const debug = true;
  if (debug) return console.log(newItem);
  if (!key) return alert('アイテム名は空欄にできません')
  loading.value = true;
  const req = await fetch('/api/ir/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ key, desc })
  });
  if (req.status != 200) {
    alert('Communication failed.');
    return false;
  }
  close_save();
  await update();
}

const editingItem = reactive({
  key: '',
  value: [],
  desc: ''
});
const editItem = (item) => {
  const { key, value, desc } = item;
  editingItem.key = key;
  editingItem.value = value;
  editingItem.desc = desc;
  edit_visible.value = true;
}
const _edit = async () => {
  const { key, desc } = editingItem;
  if (!key) return alert('アイテム名は空欄にできません')
  loading.value = true;
  const req = await fetch(`/api/ir/${key}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ desc })
  });
  if (req.status != 200) {
    alert('Communication failed.');
    return false;
  }
  close_edit();
  await update();
}

const deletingItem = reactive({
  key: ''
});
const deleteItem = (item) => {
  deletingItem.key = item.key;
  delete_visible.value = true;
}
const _delete = async (_key = null, standalone = false) => {
  loading.value = true;
  let { key } = deletingItem;
  if (_key) key = _key;
  const req = await fetch(`/api/ir/${key}`, {
    method: 'DELETE'
  });
  if (req.status != 200) {
    alert('Communication failed.')
    return false;
  }
  if (!standalone) {
    close_delete();
    await update();
  }
}

const deleteMulti = async () => {
  if (!confirm('本当に削除しますか？')) return;
  loading.value = true;

  await Promise.all(
    itemsSelected.value.map(item => _delete(item.key, true))
  );

  close_delete();
  await update();
}

update();

</script>


<style scoped>
h1 {
  font-weight: 500;
  font-size: 2.6rem;
  position: relative;
  top: -10px;
}

h3 {
  font-size: 1.2rem;
}

.signal {
  display: grid;
  grid-template-columns: repeat(auto-fill, 3.85em);
}
.signal_item {
  background: #f6f6f6;
  box-shadow: 1px 1px 0.1em #aaa;
  color: #666;
  display: inline-block;
  font-family: courier, monospace;
  font-weight: bold;
  margin: 0.2em;
  padding: 0.1em 0.1em;
  text-align: right;
}

.greetings h1,
.greetings h3 {
  text-align: center;
}

.darkbox {
  background: rgba(43, 43, 43, .9);
  border-radius: 0.35em;
  color: #fff;
  position: fixed;
  top: 25%;
  left: 0;
  right: 0;
  margin: auto;
  max-width: 400px;
  padding: 0.75em 1em;
  z-index: 3;
}
.btns {
  display: flex;
  height: 3em;
  justify-content: space-evenly;
  padding: 1em 0 0;
}
@media (min-width: 1024px) {
  .greetings h1,
  .greetings h3 {
    text-align: left;
  }
}
</style>
