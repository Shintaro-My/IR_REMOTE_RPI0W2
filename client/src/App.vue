<script setup>
import { ref } from "vue";
import { RouterLink, RouterView } from 'vue-router'

const luminance = ref(NaN);
const _run = ref(true);
const active = ref(false);

const _ = (async()=>{
  while (_run.value) {
    await new Promise(r => setTimeout(r, 1000));
    if (!active.value) continue;
    let num = NaN;
    try {
      const req = await fetch('/api/cds');
      const { value } = await req.json();
      num = value || NaN;
    } catch(e) {
      console.log(e);
    }
    luminance.value = num;
  }
  return true;
})();
console.log(_);

</script>

<template>
  <header>
    <!--<img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />-->

    <div class="luminance" :style="`--val: ${luminance / 10}`">
      <div class="value">
        {{ luminance }}
      </div>
    </div>
    
    <div class="wrapper">
      <div class="util">
        <button class="btn btn-radius-solid" @click="active = !active">{{ active ? '停止' : '取得' }}</button>
      </div>
      <nav>
        <RouterLink to="/irtable">信号一覧</RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>

<style scoped>
header {
  line-height: 1.5;
  max-height: 100vh;
}

.luminance {
  --val: 0;
  align-items: center;
  background: rgb(100, 40, calc(var(--val) * 2 + 20));
  border-radius: 150px;
  box-shadow: 1px 1px 3px #aaa, 0px 1px 3px #aaa;
  display: flex;
  height: 150px;
  justify-content: center;
  margin: 0.35em;
  width: 150px;
}

.luminance > .value {
  color: #fff;
  font-family: courier, monospace;
  font-size: 1.3em;
  font-weight: bold;
  text-align: center;
  text-shadow: 1px 1px 2px #333;
}


nav {
  width: 100%;
  font-size: 12px;
  text-align: center;
  margin-top: 2rem;
}

nav a.router-link-exact-active {
  color: var(--color-text);
}

nav a.router-link-exact-active:hover {
  background-color: transparent;
}

nav a {
  display: block;
  padding: 0 1rem;
  border-left: 1px solid var(--color-border);
}

nav a:first-of-type {
  border: 0;
}

@media (min-width: 1024px) {
  header {
    display: flex;
    place-items: center;
    padding-right: calc(var(--section-gap) / 2);
  }

  .logo {
    margin: 0 2rem 0 0;
  }

  header .wrapper {
    display: flex;
    place-items: flex-start;
    flex-wrap: wrap;
  }

  nav {
    text-align: left;
    font-size: 1rem;

    padding: 1rem 0;
    margin-top: 1rem;
  }
}
</style>
