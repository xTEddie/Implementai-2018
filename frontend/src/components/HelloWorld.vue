<template>
  <div class="wrapper">
    <!-- <video v-for="(vid,index) in vid_json" :key="index">
      <source :src="vid" type="video/mp4">
    </video> -->
    <!-- <figure v-for="(img, index) in img_json" :key="index">
      <img src="@/assets/test_img.jpg">
    </figure> -->
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: '',
  data() {
    return {
    }
  },
  props: {
  },
  methods: {
    get_users() {
      axios.get('http://localhost:8000/users').then((response) => {
        console.log(response.data)
      })
    },
    get_videos() {
      
    }
  },
  created() {
    this.get_videos()
    //this.get_users()
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.wrapper {
    position: relative;
    display: grid;
    padding-bottom: 5rem;
    padding-top: 5vh;
    grid-template-columns: repeat(3, 30vw);
    grid-template-rows: repeat(3, 30vw);
    grid-column-gap: 15px;
    grid-row-gap: 15px;
    justify-items: center;
    border: 2px solid #2B9DFF;
}

video {
  position: relative;
  overflow: hidden;
  margin:0;
  width: auto;
  height: 30vh;
  background-color: white;
}
</style>
