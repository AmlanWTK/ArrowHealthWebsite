import sys

html_content = """
          <!-- Dr. Indrajit Prosad -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./appimages/prof.-dr.-indrajit prasad-1.png');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Professor Dr. Indrajit Prasad</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Dr. Farid Uddin -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./appimages/Dr. Farid Uddin.jpeg');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Professor Mohammad Farid Uddin</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Prof. Dr. A K M Aminul Islam -->
          <div class="expert-card">
            <div class="expert-status secondary">Next slot: Tomorrow</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./appimages/Prof. Dr. A K M Aminul Islam.jpeg');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Prof. Dr. A K M Aminul Islam</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Faria Afsana -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./assets/Directory of Endrocrinologists in Bangladesh/Dr. Faria Afsana/Faria-Afsana.webp');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Dr. Faria Afsana</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Shahajada Selim -->
          <div class="expert-card">
            <div class="expert-status secondary">Next slot: Tomorrow</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./assets/Directory of Endrocrinologists in Bangladesh/Dr. Shahjada Selim/Shahjada-Selim.webp');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Dr. Shahjada Selim</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>

          <!-- Prof Faruque Pathan -->
          <div class="expert-card">
            <div class="expert-status available">✓ Available Today</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-image: url('./assets/Directory of Endrocrinologists in Bangladesh/Professor Md. Faruque Pathan/Faruq_pathan-removebg-preview_1711966760.png');"></div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Professor Md. Faruque Pathan</h3>
              <span class="expert-credentials">Endocrinologist</span>
              <p>Specialist in endocrinology, diabetes care, and metabolic health management.</p>
              <div class="expert-action-row"><div class="expert-meta"><small>Duration</small><strong>30 Min</strong></div><button class="expert-book-btn">Book Consultation</button></div>
            </div>
          </div>
"""

with open(r'd:\carehub\arrow_health_website\index.html', 'r', encoding='utf-8') as f:
    content = f.read()

start_str = '<div class="experts-grid">'
start_idx = content.find(start_str)

if start_idx != -1:
    content_after_start = content[start_idx + len(start_str):]
    
    div_count = 1 # experts-grid is open
    i = 0
    while i < len(content_after_start) and div_count > 0:
        if content_after_start[i:i+4] == '<div':
            div_count += 1
            i += 4
        elif content_after_start[i:i+6] == '</div>':
            div_count -= 1
            i += 6
        else:
            i += 1
    
    end_idx = start_idx + len(start_str) + i - 6 # -6 to not include the closing </div> of experts-grid itself yet
    
    new_content = content[:start_idx + len(start_str)] + "\n" + html_content + "\n        " + content[end_idx:]
    with open(r'd:\carehub\arrow_health_website\index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print("Replacement using robust HTML div counting completed.")
else:
    print("Could not find <div class=\"experts-grid\">")
