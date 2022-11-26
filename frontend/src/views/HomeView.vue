<template>
  <div class="home">
    <JumboTron />
    <PreviewTable />
  </div>
</template>

<script>
// @ is an alias to /src
import JumboTron from "@/components/JumboTron.vue";
import PreviewTable from "@/components/PreviewTable.vue";

export default {
  name: 'HomeView',
  components: {
    JumboTron,
    PreviewTable
  },
  beforeMount() {
    document.title = 'OFA | Home';
  }
}
</script>


