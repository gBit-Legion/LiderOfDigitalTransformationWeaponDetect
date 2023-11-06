<template>
  <div class="rounded-lg pt-6">
    <p class="text-center pb-4 font-bold text-xl">Пример загружаемых данных</p>
    <div
      class="shadow-md sm:rounded-lg rounded-lg overflow-auto h-[500px] xl:max-w-[1800px] lg:max-w-4xl md:max-w-3xl sm:max-w-2xl mx-auto max-w-[300px]"
    >
      <table
        class="w-full text-xs text-gray-500 table-auto 2xl:table-fixed text-center"
      >
        <thead class="text-xs text-gray-700 uppercase bg-gray-50 font-bold">
          <tr class="">
            <th
              scope="col"
              class="px-1 py-3 2xl:w-96 cursor-pointer hover:text-[#e40046]"
            >
              RTSP-ссылка
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-54 cursor-pointer hover:text-[#e40046]"
            >
              Широта
            </th>
            <th
              scope="col"
              class="px-6 py-3 2xl:w-54 cursor-pointer hover:text-[#e40046]"
            >
              Долгота
            </th>
          </tr>
        </thead>
        <tbody class="font-semibold">
          <tr v-for="row in 7" :key="row">
            <td class="px-6 py-4">
              rtsp://admin:12345@192.168.1.210:554/cam/realmonitor
            </td>
            <td class="px-6 py-4">55.851233</td>
            <td class="px-6 py-4">35.32134</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>
<script>
export default {
  data() {
    return {};
  },
};
</script>
