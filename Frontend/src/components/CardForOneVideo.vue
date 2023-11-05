<template>
 
 <div class="grid-cols-1 sm:grid md:grid-cols-2 ">
  <div v-for="el in 6" :key="el"
    class="mx-3 mt-6 flex flex-col self-start rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 sm:shrink-0 sm:grow sm:basis-0">
    <video controls="controls" class="rounded-t-lg"> 
        <source src="../image/test-video.mp4">
    </video>
    <div class="p-6">
      <h5
        class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
        Видео № {{ el }}
      </h5>
      <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
        Некоторая инфа
      </p>
    </div>
    <button class="bg-blue-700 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded">
  Показать стоп-кадры
</button>
  </div>
</div>
</template>

<script>
export default {

}
</script>

<style>

</style>