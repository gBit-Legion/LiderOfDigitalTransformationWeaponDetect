<template>
  <div class="h-full">
    <div class="px-[150px]">
      <p
        class="text-idealDarkGray flex justify-center text-center text-6xl font-TT_Firs_Neue_Bold font-black h-auto pt-12 tracking-wide"
      >
        ЗАГРУЗКА АРХИВА ВИДЕОЗАПИСЕЙ
      </p>
      <p
        class="text-idealDarkGray flex justify-center text-center text-xl font-TT_Firs_Neue_Bold font-black h-auto pt-12 tracking-wide"
      >
        Используйте файл формата .zip
      </p>
      <div class="max-w-6xl mx-auto mt-4">
        <div class="relative mb-4 flex w-full items-stretch">
          <input
            v-on:change="handleFilesUpload()"
            class="relative m-0 -mr-0.5 block w-full min-w-0 flex-auto rounded-l-[7px] border-2 border-solid border-idealBlue bg-whitesmoke bg-clip-padding px-3 py-[0.25rem] text-base font-normal leading-[1.6] text-neutral-700 outline-none transition duration-200 ease-in-out focus:z-[3] focus:border-primary focus:text-neutral-700 focus:shadow-[inset_0_0_0_1px_rgb(59,113,202)] focus:outline-none"
            id="file_input"
            type="file"
            ref="files"
            accept=".zip"
          />
          <button
            class="relative z-[2] border-idealBlue rounded-r-[7px] border-2 px-4 py-2 text-sm font-medium font-TT_Firs_Neue_Regular text-whitesmoke bg-idealBlue text-gray-50 transition duration-150 ease-in-out hover:bg-black hover:bg-opacity-5 hover:text-idealBlue focus:outline-none focus:ring-0"
            type="button"
            id="button-addon4"
            @click="submitFiles()"
            data-te-ripple-init
          >
            Загрузить
          </button>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { mapActions, mapGetters } from "vuex";
import axios from "axios";
export default {
  data() {
    return {
      files: "",
    };
  },
  computed: {
    ...mapGetters(["isLoading", "error"]),
  },
  methods: {
    ...mapActions(["GET_VIDEO", "GET_LOADING", "GET_ERROR"]),
    submitFiles() {
      this.GET_LOADING(true);
      let formData = new FormData();
      for (var i = 0; i < this.files.length; i++) {
        let file = this.files[i];
        formData.append("file", file);
      }
      console.log(typeof formData);
      axios
        .post(
          `http://${process.env.VUE_APP_USER_IP_WITHPORT}/archive`,
          formData,
          {
            headers: {
              "Content-Type": "multipart/form-data",
            },
          }
        )
        .then(
          (response) => (
            console.log(response.data),
            this.GET_LOADING(false),
            console.log("ФАЙЛ УСПЕШНО ЗАГРУЖЕН!"),
            this.GET_VIDEO(JSON.parse(response.data))
          )
        )
        .catch(
          (response) => (
            console.log(response), 
            this.GET_LOADING(false), 
            this.GET_ERROR(true, response.status)
          )
        )
        .finally(function () {});
    },
    handleFilesUpload() {
      this.files = this.$refs.files.files;
    },
  },
};
</script>
