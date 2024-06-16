<template>
  <section id="team-members" class="section">
    <h2>球队成员信息</h2>
    <!-- 在此添加球队成员信息 -->
    <div class="football-team-players">
    <header class="team-header">
      <img :src="team.logo" alt="Team Logo" class="team-logo" />
      <h1 class="team-name">{{ team.name }}</h1>
    </header>
    
    <section class="players-list">
      <h2>Players</h2>
      <ul class="players">
        <li v-for="player in team.players" :key="player.id" class="player-item">
          <img :src="player.photo" alt="Player Photo" class="player-photo" />
          <div class="player-info">
            <h3 class="player-name">{{ player.name }}</h3>
            <p class="player-position">{{ player.position }}</p>
            <p class="player-bio">{{ player.bio }}</p>
          </div>
        </li>
      </ul>
    </section>
  </div>

  </section>
</template>

<script>
export default {
  name: 'TeamMembers',
  data() {
    return {
      team: {
        name: 'Manchester United',
        logo: 'https://img2.baidu.com/it/u=3820838600,563397879&fm=253&fmt=auto&app=138&f=JPEG?w=500&h=500', // 替换为球队的实际 logo 地址
        players: [
          { 
            id: 1, 
            name: 'David de Gea', 
            position: 'Goalkeeper', 
            photo: 'https://citinewsroom.com/wp-content/uploads/2018/08/102949213_de_gea_getty.jpg', // 替换为球员的实际照片地址
            bio: `
              David de Gea Quintana is a Spanish professional footballer who plays as a goalkeeper for 
              Premier League club Manchester United and the Spain national team. He joined Manchester 
              United in 2011 and has since become one of the top goalkeepers in the world.
            `
          },
          { 
            id: 2, 
            name: 'Harry Maguire', 
            position: 'Defender', 
            photo: 'https://bdimg6.qunliao.info/fastdfs5/M00/31/D9/rB8CCl8w-W2AfawLAABq2EsY35I377.jpg', // 替换为球员的实际照片地址
            bio: `
              Harry Maguire is an English professional footballer who plays as a centre-back for 
              Premier League club Manchester United and the England national team. He joined Manchester 
              United in 2019 and quickly became the team captain.
            `
          },
          { 
            id: 3, 
            name: 'Bruno Fernandes', 
            position: 'Midfielder', 
            photo: 'https://resource.ttplus.cn/publish/app/data/2021/11/06/399068/b627452d-9d89-4b87-a1e0-2f3f5b6c44e6.jpg', // 替换为球员的实际照片地址
            bio: `
              Bruno Miguel Borges Fernandes is a Portuguese professional footballer who plays as a 
              midfielder for Premier League club Manchester United and the Portugal national team. 
              He joined Manchester United in 2020 and has been instrumental in the team's midfield.
            `
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


.football-team-players {
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

.players-list {
  margin-top: 30px;
}

h2 {
  font-size: 2em;
  color: #d2232a;
  margin-bottom: 15px;
}

.players {
  list-style: none;
  padding: 0;
}

.player-item {
  display: flex;
  align-items: center;
  margin-bottom: 20px;
}

.player-photo {
  width: 50px;
  height: 50px;
  border-radius: 50%;
  margin-right: 15px;
}

.player-info {
  text-align: left;
}

.player-name {
  font-size: 1.5em;
  color: #333;
}

.player-position {
  font-size: 1.2em;
  color: #777;
}

.player-bio {
  font-size: 1.1em;
  color: #555;
  line-height: 1.4;
}
</style>
