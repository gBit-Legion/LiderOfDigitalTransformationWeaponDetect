import { createStore } from 'vuex'
import axios from 'axios'
import weapondetection from '@/store/modules/weapondetection'


export default createStore({
  
  modules: {
    weapondetection
  }
})