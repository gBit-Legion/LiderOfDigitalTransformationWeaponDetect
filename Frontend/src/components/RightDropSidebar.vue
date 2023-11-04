<template>
  <div>
    <button
      @click="showInfo = !showInfo"
      @click.stop
      class="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded"
    >
      Показать последние события
    </button>
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform translate-x-full"
      enter-to-class="transform translate-x-0"
      leave-active-class="transition ease-in duration-300"
      leave-from-class="transform translate-x-0"
      leave-to-class="transform translate-x-full"
    >
      <div
        v-if="showInfo"
        ref="infoBlock"
        class="fixed inset-y-0 right-0 w-1/4 bg-white shadow-lg"
      >
      <div v-for="(el, index) in events" :key="index">
        <img src="https://gpvn.ru/files/2022/08/vn08830.jpg" alt="Фото с улицы" class="mt-5" />
        <div class="p-4">
          <h2 class="text-xl font-bold mb-2">{{ el.name }}</h2>
          <p class="mt-4"><strong>Адрес обнаружения:</strong> {{ el.address }}</p>
          <p><strong>Время обнаружения:</strong> {{ el.phone }}</p>
          <p><strong>Класс обнаружения:</strong> {{el.class }}</p>
        </div>
      </div>
      </div>
    </transition>
  </div>
</template>

<script>
export default {
  data() {
    return {
      showInfo: false,
      events: [
        {
        name: "Камера №1",
        address: "Ждановская д. 13",
        phone: "07:50",
        class: "Knife",
      },
      {
        name: "Камера №1",
        address: "Ждановская д. 13",
        phone: "07:50",
       
      },
      {
        name: "Камера №1",
        address: "Ждановская д. 13",
        phone: "07:50",
       
      }
    ] ,
    };
  },
  mounted() {
    document.addEventListener("click", this.handleClickOutside);
  },
  beforeUnmount() {
    document.removeEventListener("click", this.handleClickOutside);
  },
  methods: {
    handleClickOutside(event) {
      if (!this.$refs.infoBlock.contains(event.target)) {
        this.showInfo = false;
      }
    },
  },
};
</script>

<style></style>
