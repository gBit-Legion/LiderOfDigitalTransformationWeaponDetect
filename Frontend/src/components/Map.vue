<template>
  <div>
  <div class="border-idealBlue border-[6px] rounded-lg shadow-cards">
    <yandex-map :coords="coords" :use-object-manager="true" :object-manager-clusterize="true"
      :settings="settings" :zoom="12" :cluster-options="clusterOptions">
      <ymap-marker v-for="item in camera_list" :key="item.id" :coords="[item.latitude, item.longitude]"
        :markerId="item.id" :cluster-name="1" :icon="markerIconCAMERA" :balloon-template="balloonTemplateCamera(item)" />
     
    </yandex-map>
  </div>
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
  
mounted() {
  },
  data() {
    return {
      player: null,
      playerOptions: {
        autoplay: true,
        controls: true,
        fluid: true,
      },
      video_url: `http://${process.env.VUE_APP_USER_IP_WITHPORT}/serve/0`,
      camera_list: [
        {
          id: 1,
          latitude: 59.957953,
          longitude: 30.299006,
          name: `Камера наблюдения`,
          address: 'Ваш адрес',
          video_url:  `http://${process.env.VUE_APP_USER_IP_WITHPORT}/serve/0`
        },
        {
          id: 2,
          latitude: 59.98,
          longitude: 30.299006,
          name: `Камера наблюдения`,
          address: 'Ваш адрес',
          video_url:  `http://${process.env.VUE_APP_USER_IP_WITHPORT}/serve/0`
        },
        {
          id: 3,
          latitude: 59.98,
          longitude: 30.32,
          name: `Камера наблюдения`,
          address: 'Ваш адрес',
          video_url:  `http://${process.env.VUE_APP_USER_IP_WITHPORT}/serve/0`
        }
      ],
      police_list: [
        {
          id: 1,
          latitude: 54.83,
          longitude: 39.832,
          name: `Имя`,
          phone: '+7(999)232-23-42',
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
      coords: [59.957953,30.299006 ],
      settings: settings,
      markerIconPOLICE: {
        layout: "default#imageWithContent",
        imageHref: "https://cdn-icons-png.flaticon.com/128/1417/1417975.png",
        imageSize: [43, 43],
        imageOffset: [0, 0],
        contentOffset: [0, 15],
      },
      markerIconCAMERA: {
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
    balloonTemplateCamera(item) {
      return `
    <h1 class="text-idealBlue text-xl font-bold font-TT_Firs_Neue_Regular">${item.name
        }</h1>
       <div>
    <img src="${item.video_url}">
  </div>
    <a class="font-semibold font-TT_Firs_Neue_Regular text-base">Адрес: ${item.address
        }</a>
  `;
    },
    

  },

}
</script>

<style>
.video-js {
  width: 100%;
  height: auto;
}
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
