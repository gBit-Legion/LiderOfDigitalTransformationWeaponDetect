<template>
  <div class="border-idealBlue border-[6px] rounded-lg shadow-cards">
    <yandex-map @click="changeMyPos" :coords="coords" :use-object-manager="true" :object-manager-clusterize="true"
      :settings="settings" :zoom="5" :cluster-options="clusterOptions">
      <ymap-marker v-for="item in postamat_list" :key="item.id" :coords="[item.latitude, item.longitude]"
        :markerId="item.id" :cluster-name="1" :icon="markerIconBANK" :balloon-template="balloonTemplate(item)" />
    </yandex-map>

  </div>
</template>

<script>
import { yandexMap, ymapMarker, loadYmap } from "vue-yandex-maps";
import { mapActions, mapGetters } from 'vuex';

const settings = {
  apiKey: "9b855f9b-6853-4cb2-b2f8-f02951d693c4",
  lang: "ru_RU",
  coordorder: "latlong",
  enterprise: false,
  version: "2.1",
};

export default {
  components: { yandexMap, ymapMarker },
  computed: {
    ...mapGetters(['selected_filter']),



  },
  async mounted() {
    const settings = {
      ...this.settings
    };
    await loadYmap({ settings, debug: true });
    this.ymaps_user = ymaps
  },
  data() {
    return {
      postamat_list: [
        {
          id: 1,
          latitude: 54.82896654088406,
          longitude: 39.831893822753904,
          name: `Камера наблюдения`,
          address: 'Можайка',
        }
      ],
      choosed_bank: '',
      map: null,
      ymaps_user: null,
      markerfill_in: {
        enabled: true,
        color: "#B22222",
        opacity: 0.5,
      },
      markerstroke_in: {
        color: "#8B0000",
        opacity: 0.5,
        width: 2,
      },
      my_coords: [
        54.82896654088406,
        39.831893822753904
      ],
      coords: [55.753215, 36.622504],
      settings: settings,
      markerIconUSER: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/10345/10345653.png",
        imageSize: [40, 40],
        imageOffset: [-20, -20],
        contentOffset: [0, 0],
      },
      markerIconATM: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/6059/6059866.png",
        imageSize: [43, 43],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },
      markerIconBANK: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/5388/5388782.png",
        imageSize: [24, 24],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },

      clusterOptions: {
        1: {
          preset: 'islands#darkGreenClusterIcons',
          clusterDisableClickZoom: false,
          clusterOpenBalloonOnClick: true,
          clusterBalloonLayout: [
            "<ul class=list>",
            "{% for geoObject in properties.geoObjects %}",
            '<li><a href=# class="list_item">{{ geoObject.properties.balloonContentHeader|raw }}</a></li>',
            "{% endfor %}",
            "</ul>",
          ].join(""),
        },
      },
    };
  },
  methods: {
    ...mapActions(['GET_MYCOORDS']),
    balloonTemplate(item) {
      return `
    <h1 class="text-idealBlue text-xl font-bold font-TT_Firs_Neue_Regular">${item.name
        }</h1>
        <iframe width="420" height="345" src="https://www.youtube.com/embed/tgbNymZ7vqY">
</iframe>
    <a class="font-semibold font-TT_Firs_Neue_Regular text-base">Адрес: ${item.address
        }</a>
  `;
    },

  },

}
</script>

<style>
.red {
  color: red;
}

.ymap-container {
  width: 100%;
  height: 76vh;
}

.ballon_header {
  font-size: 16px;
  margin-top: 0;
  margin-bottom: 10px;
  color: #708090;
}

.ballon_body {
  font-size: 14px;
  text-align: center;
}

.ballon_footer {
  font-size: 12px;
  text-align: right;
  border-top: 1px solid #7d7d7d;
  color: #7d7d7d;
  margin-top: 10px;
}

.description {
  display: block;
  color: #999;
  font-size: 10px;
  line-height: 17px;
}
</style>
