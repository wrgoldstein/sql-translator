<script>
  // import {onMount} from 'svelte'

  import svelteLogo from './assets/svelte.svg'
  import viteLogo from '/vite.svg'
  import Counter from './lib/Counter.svelte'
  
  let show_info = false
</script>

<main>
  <h1>SQL Transpiler</h1>
  <button on:click={() => show_info = !show_info}>ⓘ</button>
  {#if show_info}
    <p style="max-width: 440px;">This is a simple web app exposing the transpilation functionality of the wonderful <a class="link" href="https://github.com/tobymao/sqlglot">sqlglot</a> package, for those of us who can only remember one SQL dialect at a time.</p>
  {/if}
  <div class="card">
    <Counter />
  </div>
</main>

<style>
.centered {
  display: flex;
  justify-content: center;
  align-items: center;
}

.link {
  padding-left: 1em;
  color: black;
  text-decoration: none;
}
</style>
