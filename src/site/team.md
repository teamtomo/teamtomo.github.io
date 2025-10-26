---
title: ""
---
# Core Team

*teamtomo* is a developed and maintained by a distributed group of volunteers from 
the cryo-EM/ET community.

<div class="team-grid" id="teamGrid">
  <div class="team-member">
    <h3>Ben Barad</h3>
  </div>
  <div class="team-member">
    <h3>Alister Burt</h3>
  </div>
  <div class="team-member">
    <h3>Marten Chaillet</h3>
  </div>
  <div class="team-member">
    <h3>Oscar Despard</h3>
  </div>
  <div class="team-member">
    <h3>Josh Dickerson</h3>
  </div>
  <div class="team-member">
    <h3>Johannes Elferich</h3>
  </div>
  <div class="team-member">
    <h3>Utz Ermel</h3>
  </div>
  <div class="team-member">
    <h3>Matthew Giammar</h3>
  </div>
  <div class="team-member">
    <h3>Pavol Harar</h3>
  </div>
  <div class="team-member">
    <h3>Mikel Izeta</h3>
  </div>
  <div class="team-member">
    <h3>Mart Last</h3>
  </div>
  <div class="team-member">
    <h3>Dennis Michalak</h3>
  </div>
  <div class="team-member">
    <h3>Braxton Owens</h3>
  </div>
  <div class="team-member">
    <h3>Ricardo Righetto</h3>
  </div>
  <div class="team-member">
    <h3>Spencer Rothfuss</h3>
  </div>
  <div class="team-member">
    <h3>Jonathan Schwartz</h3>
  </div>
  <div class="team-member">
    <h3>Pranav Shah</h3>
  </div>
  <div class="team-member">
    <h3>Liza Shiltseva</h3>
  </div>
  <div class="team-member">
    <h3>Davide Torre</h3>
  </div>
  <div class="team-member">
    <h3>Aysecan Unal</h3>
  </div>
  <div class="team-member">
    <h3>Abigail Watson</h3>
  </div>
</div>
<div align="center">
(alphabetical by last name)
</div>

<style>
.team-grid {
  display: flex;
  flex-wrap: wrap;
  gap: 0.5rem;
  padding: 1rem 0;
  justify-content: center;
}

.team-member {
  flex: 0 0 140px; /* Fixed width to fit longest name */
  background: var(--md-code-bg-color);
  border-radius: 6px;
  padding: 0.5rem 0.75rem;
  text-align: center;
  transition: transform 0.2s, box-shadow 0.2s;
  white-space: nowrap;
  overflow: hidden;
  text-overflow: ellipsis;
}

.team-member:hover {
  transform: translateY(-2px);
  box-shadow: 0 4px 8px rgba(0,0,0,0.1);
}

.team-member h3 {
  margin: 0;
  font-size: 0.65rem;
  color: var(--md-primary-fg-color);
  font-weight: 500;
}

/* Dynamic width classes */
.team-member.cols-3 { flex: 0 1 calc(33.333% - 0.333rem); max-width: 200px; }
.team-member.cols-4 { flex: 0 1 calc(25% - 0.375rem); max-width: 180px; }
.team-member.cols-5 { flex: 0 1 calc(20% - 0.4rem); max-width: 160px; }
.team-member.cols-6 { flex: 0 1 calc(16.666% - 0.417rem); max-width: 140px; }
.team-member.cols-7 { flex: 0 1 calc(14.285% - 0.429rem); max-width: 130px; }

@media (max-width: 768px) {
  .team-member {
    flex: 1 1 calc(50% - 0.25rem);
    max-width: none;
  }
}

@media (max-width: 480px) {
  .team-member {
    flex: 1 1 100%;
    max-width: none;
  }
}
</style>

<script>
function distributeTeamMembers() {
  const grid = document.getElementById('teamGrid');
  if (!grid) return;
  
  const members = Array.from(grid.querySelectorAll('.team-member'));
  const totalMembers = members.length;
  
  // Calculate container width
  const containerWidth = grid.offsetWidth;
  const minItemWidth = 140; // Minimum width to fit longest names
  const gap = 8; // 0.5rem gap
  
  // Calculate maximum possible columns
  const maxCols = Math.floor((containerWidth + gap) / (minItemWidth + gap));
  
  // Find optimal column count that distributes members evenly
  let bestCols = maxCols;
  let minDifference = totalMembers;
  
  for (let cols = Math.min(maxCols, 7); cols >= 3; cols--) {
    const rows = Math.ceil(totalMembers / cols);
    const lastRowItems = totalMembers % cols || cols;
    const difference = cols - lastRowItems;
    
    // Prefer layouts where the last row has at least cols-2 items
    if (lastRowItems >= cols - 2 && difference < minDifference) {
      minDifference = difference;
      bestCols = cols;
    }
  }
  
  // Apply the column class to all members
  members.forEach(member => {
    // Remove any existing cols classes
    member.className = member.className.replace(/\bcols-\d+\b/g, '');
    member.classList.add(`cols-${bestCols}`);
  });
}

// Run on load and resize
if (typeof window !== 'undefined') {
  window.addEventListener('load', distributeTeamMembers);
  window.addEventListener('resize', () => {
    clearTimeout(window.resizeTimer);
    window.resizeTimer = setTimeout(distributeTeamMembers, 250);
  });
  
  // Run immediately if DOM is already loaded
  if (document.readyState === 'complete' || document.readyState === 'interactive') {
    setTimeout(distributeTeamMembers, 0);
  }
}
</script>
