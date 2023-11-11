<script setup>
import { ref } from "vue";
import { RouterLink, RouterView } from 'vue-router'

const luminance = ref(0);
const active = ref(true)

const _ = (async()=>{
  while (active.value) {
    let num = 0;
    try {
      const req = await fetch('/api/cds');
      num = (await req.json())?.value || 0;
    } catch(e) {
      console.log(e);
    }
    luminance.value = num;
    await new Promise(r => setTimeout(r, 1000));
  }
  return true;
})();
console.log(_);

</script>

<template>
  <header>
    <!--<img alt="Vue logo" class="logo" src="@/assets/logo.svg" width="125" height="125" />-->

    <div class="luminance">
      <div class="value">
        {{ luminance }}
      </div>
    </div>
    
    <div class="wrapper">
      <div class="util">
        <button class="btn btn-radius-solid" @click="console.log">ドアを開錠する</button>
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
  height: 150px;
  width: 150px;
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
