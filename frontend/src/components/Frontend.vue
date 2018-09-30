<template>
<div>
  <div class="wrapper">
    <video v-for="(vid,index) in videos" :class="(isViolent[index.toString()]) ? 'danger':'grayscale'" :key="index" loop>
      <source :src="vid.path" type="video/mp4">
    </video>
  </div>
</div>

</template>

<script>
import axios from 'axios'

export default {
  name: '',
  data() {
    return {
      videoElements: [],
      video_data:[],
      videos: {},
      isViolent: {
        '0': false,
        '1': false,
        '2': false,
        '3': false,
        '4': false,
        '5': false,
        '6': false,
        '7': false,
        '8': false,
        '9': false,
        '10': false,
        '11': false,
        '12': false,
        '13': false
      },
    }
  },
  props: {
  },
  methods: {
    get_videos() {
      axios.get('http://localhost:8000/videos').then((response) => {
        this.videos = response.data
        console.log(response.data)
      })
    },
    get_video_data() {
      axios.get('http://localhost:8000/videoframes').then((response) => {
        this.video_data = response.data
      })
    },
    play_video() {
      let videos = document.getElementsByTagName("video")
      for (let i =0;i<videos.length; i++) {
        videos[i].play();
      }
      //sample every 0.5s
      setInterval(this.sampling, 500);   
    },
    sampling() {
      console.log('sample');
      let videos = document.getElementsByTagName("video")
      for (let i =0;i<videos.length; i++) {
        let video_time = videos[i].currentTime;
        let video_id = i+1;
        let violence_status = this.find_sample_value(video_id,video_time)
        this.isViolent[i.toString()] = violence_status
        console.log(`id: ${video_id}, time: ${video_time}, violence_status: ${violence_status}`)
        console.log(this.isViolent)
      }      
    },
    find_sample_value(video_id, video_time) {
      for (let i=0; i< this.video_data.length; i++) {
        if (this.video_data[i].video.id == video_id && (this.video_data[i].current_second <= video_time+0.2 && this.video_data[i].current_second >= video_time-0.2)) {
          return this.video_data[i].violence_status
        }
      }
    }
  },
  created() {
    this.get_videos()
    this.get_video_data()
  },
  mounted() {
    document.addEventListener("keydown", (e) => {
      if (e.keyCode === 13) {  //checks whether the pressed key is "Enter"
          this.play_video()
      }   
    }) 
  }
}
</script>

<style scoped>
.wrapper {
    position: relative;
    display: grid;
    grid-template-columns: repeat(4, 24vw);
    grid-template-rows: repeat(4, 20vw);
    grid-column-gap: 2px;
    grid-row-gap: 2px;
    overflow: hidden;
    justify-items: center;
    /* border: 2px solid #2B9DFF; */
}

video {
  position: relative;
  overflow: hidden;
  margin:0;
  width:100%;
  height: auto;
  transition: all .5s;
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
