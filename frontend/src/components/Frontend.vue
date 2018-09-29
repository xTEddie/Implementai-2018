<template>
<div>
  <button v-on:click="play_video()">Play All Videos</button>
  <div class="wrapper">
    <video :class="(isViolent) ? 'danger':'grayscale'" v-for="(vid,index) in videos" :key="index" loop>
      <source :src="vid.path" type="video/mp4">
    </video>
    <!-- <figure v-for="(img, index) in img_json" :key="index">
      <img src="@/assets/test_img.jpg">
    </figure> -->
  </div>
</div>

</template>

<script>
import axios from 'axios'

export default {
  name: '',
  data() {
    return {
      videos: {},
      isViolent: false,
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
      axios.get('http://localhost:8000/videos').then((response) => {
        this.videos = response.data
        console.log(response.data)
      })
    },
    play_video() {
      let videos = document.getElementsByTagName("video")
      for (let i =0;i<videos.length; i++) {
        videos[i].play();
      }
    }
  },
  created() {
    this.get_videos()
  }
}
</script>

<style scoped>
.wrapper {
    position: relative;
    display: grid;
    padding-bottom: 5rem;
    padding-top: 0vh;
    grid-template-columns: repeat(3, 30vw);
    grid-template-rows: repeat(3, 30vw);
    grid-column-gap: 15px;
    grid-row-gap: 15px;
    overflow: hidden;
    justify-items: center;
    /* border: 2px solid #2B9DFF; */
}

video {
  position: relative;
  overflow: hidden;
  margin:0;
  width:100%;
  height: 100%;
}

.danger {
  -webkit-filter: invert(40%) grayscale(100%) brightness(40%) sepia(100%) hue-rotate(-50deg) saturate(400%) contrast(2);
  filter: grayscale(100%) brightness(40%) sepia(100%) hue-rotate(-50deg) saturate(600%) contrast(0.8); 
}

.grayscale {
  -webkit-filter: grayscale(1);
  filter: grayscale(1); 
}
</style>
