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
 ...mapGetters(['isLoading'])
},
  methods: {

  }
}
</script>