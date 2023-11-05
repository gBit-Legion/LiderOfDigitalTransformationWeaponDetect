<template>
  <div class="grid-cols-1 sm:grid md:grid-cols-2 ">
    <div v-for="el in 6" :key="el"
      class="mx-3 mt-6 flex flex-col self-start rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 sm:shrink-0 sm:grow sm:basis-0">
      <video controls="controls" class="rounded-t-lg">
        <source src="../image/test-video.mp4">
      </video>
      <div class="p-6">
        <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
          Видео № {{ el }}
        </h5>
        <p class="mb-4 text-base text-neutral-600 dark:text-neutral-200">
          Некоторая инфа
        </p>
      </div>
      <button @click="card_isOpen = !card_isOpen, choosed_card = el"
        class="bg-blue-700 hover:bg-blue-900 text-white font-bold py-2 px-4 rounded">
        Показать стоп-кадры
      </button>
      <div v-if="card_isOpen && choosed_card == el"
        class="grid mb-8 border border-gray-200 rounded-lg shadow-sm dark:border-gray-700 md:mb-12 md:grid-cols-2">
        <figure v-for="image in 3" :key="image"
          class="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 rounded-t-lg md:rounded-t-none md:rounded-tl-lg md:border-r dark:bg-gray-800 dark:border-gray-700">
          <blockquote class="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Изображение {{ image }}</h3>
            
          </blockquote>
          <figcaption class="flex items-center justify-center space-x-3">
            <img class="w-80" src="https://gpvn.ru/files/2022/08/vn08830.jpg" alt="stop-cadr">
            
            <div class="space-y-0.5 font-medium dark:text-white text-left">
              <div>Класс: knife</div>
              
            </div>
          </figcaption>
        </figure>
        
      </div>
    </div>
  </div>
</template>

<script>
export default {


  data() {
    return {
      card_isOpen: false,
      choosed_card: -1,
    }
  },
  methods: {
  }
}
</script>

<style></style>