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
    <p>This is a simple web app exposing the transpilation functionality of sqlglot, for those of us who can only remember one SQL dialect at a time.</p>
  {/if}
  <div class="centered">
      <img style="width: 18px;" alt="img" src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACAAAAAgCAMAAABEpIrGAAAAUVBMVEVHcEz////////////////////////////X2NmrrK6QkpSChIfy8vMRGCAAAAcYHyYEDxkhJiwkKS/////j5OQyNzyanJ5vcXS3uLrIyMpYW198Vx0NAAAAFHRSTlMATpHJ6f8PpP//////////////HKkegCQAAAF4SURBVHgBfZPdsoMgDIQVWatIAqH+v/+DHjLWHoudflcZWJIFkupCbRoL2MbU1RfaB9D1bhhc3wGPttw38I6YKASKTM7DfB63cEySTogd7CXJE+NE6YM4eTzf5zGypIIQR5w5rO4TXTRClCR6e/qb8v48pyiBMkFimmdKYYI5CriYEgPow+L63i2yAuCU4gwt8vA5lgkFSfIp/8gCOL0AoSDq4oz8vgiirlBAuppQV2ZkvfaGgk1T8GiqZs2RBNzQxHFtKqsWwoIbS1ATtsKQgzDghq6Tgwp+ZHA4SsiEG5McJZqe1K5Hged0mDSdRuTuFl7XrMH6Ilw8xKbHJKKu1KVMkXjGBcfpyKufNTL1GLJkcR4Z7xZWX+dntVgCD9hJ4g4lh6/OHI6eMojCIxZOLx/rIRA6W9t2HPbinzLc2XfTrkz7Nnb+IhDe0P63/cYUmc8SWRC4w/M6OH7nEN+CwLu3bTF6235m2HjvYL4Mr8cLXw7vr/H/AxR9JCllSTWqAAAAAElFTkSuQmCC">
      <a class="link" href="https://github.com/tobymao/sqlglot">https://github.com/tobymao/sqlglot</a>
  </div>  
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
