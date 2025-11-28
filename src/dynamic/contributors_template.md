---
title: ""
hide:
---
# Contributors

<div class="team-grid">
  {% for member in contributors %}
  <img src="https://avatars.githubusercontent.com/{{ member.github }}" alt="{{ member.name|default(member.github, true) }}" class="avatar-img">  
  <p style="text-align: center;">
    <b><a href="https://github.com/{{ member.github }}" target="_blank">{{ member.name|default(member.github, true) }}</a></b><br>
    {% for repo in member.repos %}
    <a href="https://github.com/teamtomo/{{ repo }}">{{ repo }}</a>{% if not loop.last %}, {% endif %}
    {% endfor %}
    {% if member.more_repos %}
    and {{ member.more_repos }} more
    {% endif %}
  </p>
  {% endfor %}
</div>

<style>
.avatar-img {
  width: 120px;
  height: 120px;
  border-radius: 50%;
  object-fit: cover;
  display: block;
  margin: auto auto;
}

.team-grid {
  display: grid;
  grid-template-columns: 160px auto;
  gap: 20px;
  margin: 20px 0;
}

/* Make it responsive - single column on small screens */
@media (max-width: 768px) {
  .team-grid {
    grid-template-columns: 1fr;
  }
}
</style>
