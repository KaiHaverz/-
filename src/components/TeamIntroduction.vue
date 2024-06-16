<template>
  <section id="team-introduction" class="section">
    <h2>球队介绍</h2>
    <!-- 在此添加球队介绍内容 -->
    <div class="football-team-introduction">
    <header class="team-header">
      <img :src="team.logo" alt="Team Logo" class="team-logo" />
      <h1 class="team-name">{{ team.name }}</h1>
    </header>
    
    <section class="team-history">
      <h2>Team History</h2>
      <p class="history-description">{{ team.history }}</p>
    </section>
    
    <section class="team-background">
      <h2>Team Background</h2>
      <p class="background-description">{{ team.background }}</p>
    </section>
    
    <section class="team-culture">
      <h2>Team Culture</h2>
      <p class="culture-description">{{ team.culture }}</p>
    </section>
  </div>
  <!----------->
  </section>
</template>

<script>
export default {
  name: 'TeamIntroduction',
  //--------------------------
  data() {
    return {
      team: {
        name: 'Manchester United',
        logo: 'https://img2.baidu.com/it/u=3820838600,563397879&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500', // 替换为球队的实际 logo 地址
        history: `
          Manchester United Football Club, commonly known as Man United or simply United, 
          is a professional football club based in Old Trafford, Greater Manchester, England.
          It was founded in 1878 as Newton Heath LYR Football Club and became Manchester United in 1902.
          Manchester United is one of the most successful and widely supported football teams in the world.
        `,
        background: `
          Manchester United has a rich history in English and European football, having won numerous 
          domestic league titles, FA Cups, League Cups, and European trophies including multiple UEFA Champions League titles.
          The club's home ground is Old Trafford, which has been its home since 1910.
        `,
        culture: `
          Manchester United has a strong cultural influence both on and off the field. The club's fanbase, known as 
          "Red Devils," is globally recognized for its passion and loyalty. The team's playing style and commitment 
          to youth development are integral parts of its identity.
        `
      }
    };
  }
  //-------------------------------------
}
</script>

<style scoped>
.section {
  padding: 20px;
}





.football-team-introduction {
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

.team-history,
.team-background,
.team-culture {
  margin-bottom: 30px;
}

h2 {
  font-size: 2em;
  color: #d2232a;
  margin-bottom: 15px;
}

p {
  font-size: 1.2em;
  color: #333;
  line-height: 1.6;
}
</style>
