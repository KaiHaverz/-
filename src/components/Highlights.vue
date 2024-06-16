<template>
  <section id="highlights" class="section">
    <h2>精彩片段</h2>
    <!-- 在此添加精彩片段内容 -->
    <div class="football-team-highlights">
    <header class="team-header">
      <img :src="team.logo" alt="Team Logo" class="team-logo" />
      <h1 class="team-name">{{ team.name }}</h1>
    </header>
    
    <section class="highlights-list">
      <h2>Highlights</h2>
      <ul class="highlights">
        <li v-for="highlight in team.highlights" :key="highlight.id" class="highlight-item">
          <h3 class="highlight-title">{{ highlight.title }}</h3>
          <iframe
            :src="highlight.videoUrl"
            frameborder="0"
            allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture"
            allowfullscreen
            class="highlight-video"
          ></iframe>
          <p class="highlight-description">{{ highlight.description }}</p>
        </li>
      </ul>
    </section>
  </div>


  </section>
</template>

<script>
export default {
  name: 'HighLights',
  data() {
    return {
      team: {
        name: 'Manchester United',
        logo: 'https://img2.baidu.com/it/u=3820838600,563397879&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500', // 替换为球队的实际 logo 地址
        highlights: [
          { 
            id: 1, 
            title: 'Manchester United vs. Chelsea Highlights', 
            videoUrl: 'https://www.bilibili.com/video/BV1ER4y147ds?t=37.4', // 替换为实际视频 URL
            description: 'Highlights from the thrilling match between Manchester United and Chelsea.'
          },
          { 
            id: 2, 
            title: 'Top Goals of the Season', 
            videoUrl: 'https://www.bilibili.com/video/BV1S4411a7nH?t=94.6', // 替换为实际视频 URL
            description: 'A compilation of the best goals scored by Manchester United this season.'
          },
          { 
            id: 3, 
            title: 'Memorable Moments', 
            videoUrl: 'https://www.bilibili.com/video/BV1tP4y157Di?t=1.6', // 替换为实际视频 URL
            description: 'Relive some of the most memorable moments in Manchester United history.'
          }
        ]
      }
    };
  }


}
</script>

<style scoped>
.section {
  padding: 20px;
}

.football-team-highlights {
  font-family: 'Arial', sans-serif;
  margin: 0 auto;
  width: 100%;
  padding: 20px;
  text-align: center;
  background-color: #f4f4f9;
}

.team-header {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-bottom: 20px;
}

.team-logo {
  width: 100px;
  height: auto;
}

.team-name {
  font-size: 2.5em;
  color: #d2232a;
}

.highlights-list {
  margin-top: 30px;
}

h2 {
  font-size: 2em;
  color: #d2232a;
  margin-bottom: 15px;
}

.highlights {
  list-style: none;
  padding: 0;
}

.highlight-item {
  margin-bottom: 30px;
}

.highlight-title {
  font-size: 1.5em;
  color: #333;
  margin-bottom: 10px;
}

.highlight-video {
  width: 100%;
  height: 400px;
  border-radius: 8px;
  margin-bottom: 10px;
  
}

.highlight-description {
  font-size: 1.1em;
  color: #555;
  line-height: 1.4;
}
</style>
