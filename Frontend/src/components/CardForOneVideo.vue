<template>
  <div class="grid-cols-1 sm:grid md:grid-cols-2 ">
    <div v-for="(el, index) in url_list" :key="index"
      class="mx-3 mt-6 flex flex-col self-start rounded-lg bg-white shadow-[0_2px_15px_-3px_rgba(0,0,0,0.07),0_10px_20px_-2px_rgba(0,0,0,0.04)] dark:bg-neutral-700 sm:shrink-0 sm:grow sm:basis-0">
      <video controls="controls" class="rounded-t-lg">
        <source type="video/mp4" :src="el">
      </video>
      <div class="p-6">
        <h5 class="mb-2 text-xl font-medium leading-tight text-neutral-800 dark:text-neutral-50">
          Видео № {{ index + 1 }}
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
        <figure v-for="(image, index) in jsonList" :key="index"
          class="flex flex-col items-center justify-center p-8 text-center bg-white border-b border-gray-200 rounded-t-lg md:rounded-t-none md:rounded-tl-lg md:border-r dark:bg-gray-800 dark:border-gray-700">
          <blockquote class="max-w-2xl mx-auto mb-4 text-gray-500 lg:mb-8 dark:text-gray-400">
            <h3 class="text-lg font-semibold text-gray-900 dark:text-white">Изображение "{{ image.name }}"</h3>
          </blockquote>
          <figcaption class="flex items-center justify-center space-x-3">
            <img @click="image_click(image)" class="w-80" :src="image.url" alt="stop-cadr">
            <div class="space-y-0.5 font-medium dark:text-white text-left">
              <div>Класс: {{image.class}}</div>
            </div>
          </figcaption>

        </figure>

      </div>
    </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'
export default {

  mounted() {
    this.video_list
  },
  data() {
    return {
      card_isOpen: false,
      choosed_card: -1,
      choosed_images: [],
      url_list: [],
      image_list: [
        
    ],
      class_list: [

      ],
      jsonList: []
    }
  },
  methods: {
    image_click(img_name) {
      this.choosed_images.push(img_name)
    }
  },
  computed: {
    ...mapGetters(['allvideos']),
    video_list() {
      this.allvideos.forEach(element => {
        this.url_list.push(`http://${process.env.VUE_APP_USER_IP_WITHPORT}${element.url}`),
        this.jsonList.push(JSON.parse(JSON.stringify({url: `http://${process.env.VUE_APP_USER_IP_WITHPORT}${element.image.image_url}`, class: element.image.class_name, name: element.image.image_name})))
        console.log(this.jsonList)
      });
    },
  }
}
</script>

<style></style>