<template>
  <div class="md:ml-64 pt-[70px] font-Montserrat">
    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div
        class="md:px-5 py-4 h-full bg-white"
        v-show="$attrs.activeindex === 0"
      >
        <div class="mb-4">
          <Map :postamat_list="allpostamats"></Map>
        </div>
      </div>
    </transition>

    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div class="px-5 py-3 h-full" v-if="$attrs.activeindex === 1">
        <UploadForm />
        <UploadTableExampleVue />
      </div>
    </transition>

    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >

      <div class="px-5 py-3 h-full" v-if="$attrs.activeindex === 2">
        <VideoDet />
      </div>
    </transition>


    <transition
      enter-active-class="transition ease-out duration-300"
      enter-from-class="transform opacity-0 scale-95"
      enter-to-class="transform opacity-100 scale-100"
      leave-active-class="transition ease-in duration-75"
      leave-from-class="transform opacity-100 scale-100"
      leave-to-class="transform opacity-0 scale-95"
    >
      <div class="px-5 py-3 h-full" v-if="$attrs.activeindex === 3">
        <YOLOAnnotator />
      </div>
    </transition>
  </div>
</template>

<script>
import Map from "@/components/Map.vue";
import DropDownOffice from "@/components/DropDownOffice.vue";
import axios from "axios";
import VideoDet from "./VideoDet.vue";
import UploadForm from "@/components/UploadForm.vue";
import YOLOAnnotator from './YOLO-Annotation-Tool-master/YOLO-Annotator.vue';
import UploadTableExampleVue from './UploadTableExample.vue';

export default {
  components: {
    VideoDet,
    Map,
    UploadForm,
    DropDownOffice,
    YOLOAnnotator,
    VideoDet,
    UploadTableExampleVue
},
  props: {
    allpostamats: Object,
  },
};
</script>
