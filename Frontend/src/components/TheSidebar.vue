<template>
  <aside :class="classes">
    <div class="">
      <div class="mt-24">
        <SidebarNavItem
          v-for="(navItem, index) in navItems"
          :key="index"
          :is-active="activeIndex === index"
          @update:isActive="
            (value) => {
              activeIndex = value ? index : -1;
              $emit('updateActiveIndex', activeIndex);
            }
          "
          :label="navItem.label"
          :icon="navItem.icon"
        />
      </div>
    </div>
  </aside>
</template>

<script>
import Button from "./Button.vue";
import SidebarNavItem from "./SidebarNavItem.vue";
export default {
  components: {
    Button,
    SidebarNavItem,
  },

  computed: {
    classes() {
      return [
        "w-64",
        "fixed",
        "top-0",
        "bg-[#2F3342]",
        "z-30",
        "h-screen",
        "font-TT_Firs_Neue_Regular",
      ];
    },
  },
  data() {
    return {
      activeIndex: 0,
      navItems: [
        { label: "Карта", icon: "map" },
        { label: "Загрузить список камер", icon: "spisok" },
        { label: "Распознавание на видео", icon: "video"},
        { label: "Ручная разметка данных", icon: "flag"}
      ],
    };
  },
};
</script>
