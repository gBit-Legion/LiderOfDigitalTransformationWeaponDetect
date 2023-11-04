<template>
  <div class="bg-white">
    <Drag />
    <CardForOneVideo />
    
  </div>
</template>

<style>
@font-face {
  font-family: "TTFirsNeue-Regular";
  src: url("../fonts/TTFirsNeue-Regular.ttf");
}

@font-face {
  font-family: "TTFirsNeue-bold";
  src: url("../fonts/TTFirsNeue-Bold.ttf");
}

</style>

<script>
import Drag from './Drag.vue';
import CardForOneVideo from './CardForOneVideo.vue';
export default {
  components: {
    Drag,
    CardForOneVideo
  },

  methods: {

  }
}
</script>