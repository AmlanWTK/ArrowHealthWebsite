import sys
import re

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

          <!-- Farida Ahmed -->
          <div class="expert-card">
            <div class="expert-status secondary">Next slot: Tomorrow</div>
            <div class="expert-avatar-wrap"><div class="expert-avatar" style="background-color: #eee; display: flex; align-items: center; justify-content: center; font-size: 24px; color: #888;">👤</div></div>
            <div class="expert-info-block">
              <span class="expert-tag specialty-diabetes">Endocrinology</span>
              <h3>Dr. Farida Ahmed</h3>
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
    text = f.read()

# find experts-grid
pattern = re.compile(r'(<div class="experts-grid">)(.*?)(</div>\s*</div>\s*</div>\s*<!-- Waitlist Modal -->)', re.DOTALL)
def replacer(match):
    return match.group(1) + "\n" + html_content + "\n        " + match.group(3)

new_text = pattern.sub(replacer, text)

with open(r'd:\carehub\arrow_health_website\index.html', 'w', encoding='utf-8') as f:
    f.write(new_text)

print("Replacement done.")
