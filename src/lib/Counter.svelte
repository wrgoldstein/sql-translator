<script>
  let q;
  let transpiled;
  let write;
  let read;

  async function transpile(){
    let fetched = await fetch(`/t`, {
      method: "POST",
      body: JSON.stringify({
        q,
        goop: "doop",
        read,
        write
      })
    })
    let json = await fetched.json()
    transpiled = json.transpiled

  }

</script>
<style>
  .lang {
    height: 100px;
    width: 100%;
  }
</style>

<div>
  <datalist id="langs">
    <option>bigquery</option>
    <option>redshift</option>
    <option>snowflake</option>
    <option>postgres</option>
    <option>mysql</option>
  </datalist>
  <div class="flex">
    <label>
      Read
      <input bind:value={read} list="langs">
    </label>
    <label>
      Write
      <input bind:value={write} list="langs">
    </label>
  </div>
  <div class="flex">
    <textarea class="lang" bind:value={q}></textarea>
    <textarea class="lang" bind:value={transpiled}></textarea>
  </div>
  <button on:click={transpile}>Transpile</button>
</div>
