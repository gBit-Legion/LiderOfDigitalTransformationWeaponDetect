<template>
  <div class="bg-white">
    <UploadArchive />
    <div v-if="isLoading" class="flex items-center justify-center w-full h-full">
	<div class="flex justify-center items-center space-x-1 text-sm text-gray-700">
		 
				<svg fill='none' class="w-6 h-6 animate-spin" viewBox="0 0 32 32" xmlns='http://www.w3.org/2000/svg'>
					<path clip-rule='evenodd'
						d='M15.165 8.53a.5.5 0 01-.404.58A7 7 0 1023 16a.5.5 0 011 0 8 8 0 11-9.416-7.874.5.5 0 01.58.404z'
						fill='currentColor' fill-rule='evenodd' />
				</svg>

		 
		<div>Обработка видео. Пожалуйста, подождите...</div>
	</div>
</div>
<!-- component -->
<div v-else-if="error.status" class="h-screen w-full flex flex-col justify-center items-center bg-[#1A2238]">
	<h1 class="text-9xl font-extrabold text-white tracking-widest">{{error.code}}</h1>
	<div class="bg-[#FF6A3D] px-2 text-2xl rounded rotate-12 absolute">
		ОШИБКА :( Попробуйте еще раз
	</div>
	<button class="mt-5">
      <a
        class="relative inline-block text-sm font-medium text-[#FF6A3D] group active:text-orange-500 focus:outline-none focus:ring"
      >
        <span
          class="absolute inset-0 transition-transform translate-x-0.5 translate-y-0.5 bg-[#FF6A3D] group-hover:translate-y-0 group-hover:translate-x-0"
        ></span>

       
      </a>
    </button>
</div>
    <CardForOneVideo v-else />
  </div>
</template>

<style>


</style>

<script>
import UploadArchive from './UploadArchive.vue';
import CardForOneVideo from './CardForOneVideo.vue';
import { mapGetters } from 'vuex';
export default {
  components: {
    UploadArchive,
    CardForOneVideo
  },
  computed: {
 ...mapGetters(['isLoading', 'error'])
},
  methods: {

  }
}
</script>