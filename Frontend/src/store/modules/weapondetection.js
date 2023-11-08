import axios from 'axios'
export default {
  state: {
    archive_videos: [
    ],
    archvive_isLoading: false,
    error: {
      status: false,
      code: 0,
      }
  },
  mutations: {
    SET_VIDEOS: (state, payload) => {
      state.archive_videos = payload;
    },
    SET_VIDEOISLOADING: (state, payload) => {
      state.archvive_isLoading = payload
    },
    SET_ERROR: (state, payload) => {
      state.error = payload
    }
  },
  getters: {
    allvideos(state) {
      return state.archive_videos;
    },
    isLoading(state) {
      return state.archvive_isLoading;
    },
    error(state) {
      return state.error;
    }
   
  },
  actions: {
    // GET_ALLPOSTAMATS: async (context,  payload,  ) => {
    //   let filter = payload.map(obj => obj.name);
    //   console.log(filter.join('//'))
    //   let  postamats_list;
    //   await axios.post(`http://${process.env.VUE_APP_USER_IP_WITHPORT}/getAllBanks?lattitude=${context.state.my_coords[0]}&longitude=${context.state.my_coords[1]}&filter=${filter.join('//')}&blind=${context.state.invalid.wheelchair}&immobile=${context.state.invalid.blind}&backway=${context.state.invalid.road}`).then((response) => {
    //   postamats_list = response;
    //   })
    //   console.log(postamats_list.data);
    //   context.commit("SET_ALLPOSTAMATS", postamats_list.data);
    // },
    GET_VIDEO: (context, archive_videos) => {
      context.commit("SET_VIDEOS", archive_videos)
    },
    GET_LOADING: (context, video_isLoadng) => {
      context.commit("SET_VIDEOISLOADING", video_isLoadng)
    },
    GET_ERROR: (context, error, code) => {
      context.commit("SET_ERROR", {status: error, code: code})
    }
  }
}
