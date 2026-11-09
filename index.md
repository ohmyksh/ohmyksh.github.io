---
layout: default
---
<div style="height:0px;"></div>
<div class="bio-flex">
  <div class="bio-photo-col">
    <img src="/assets/img/profile_Nov26.jpg" style="max-width:100%; height:auto; display:block;" alt="Logo" />
    <p style="color:#000; font-size:13.5px; font-weight:350; margin-top:10px; margin-bottom:6px;">sohyeon@stanford.edu<br>sohyeon.kim@vision.snu.ac.kr</p>
    <div class="social-links" style="display:flex; flex-direction:row; flex-wrap:nowrap; white-space:nowrap; gap:8px; margin-top:0; font-size:14px;">
      <a href="https://github.com/ohmyksh" style="text-decoration:none;">Github</a>
      <a href="https://scholar.google.com/citations?user=Oe6wbtMAAAAJ&hl=en" style="text-decoration:none;">Scholar</a>
      <a href="https://www.linkedin.com/in/kimsohyeon/" style="text-decoration:none;">LinkedIn</a>
      <a href="https://x.com/ohmyksh?s=21" style="text-decoration:none;">X</a>
      <a href="{{ '/blog/' | relative_url }}" style="text-decoration:none;">Blog</a>
    </div>
  </div>
  <div class="bio-text-col">
<p style="color:#000; font-weight:300; font-size:15px; margin-bottom:12px;"> I am a visiting researcher at Stanford University, working with Prof. <a href="https://ai.stanford.edu/~cbfinn/" style="color:#0E8C8C; font-weight:450;">Chelsea Finn</a>. I am also a second-year PhD student at Seoul National University, advised by Prof. <a href="https://vision.snu.ac.kr/gunhee/" style="color:#0E8C8C; font-weight:450;">Gunhee Kim</a>.</p>

<p style="color:#000; font-weight:300; font-size:15px; margin-bottom:12px;">
  I have always been drawn to what I know, what I do not, and how to explore the gap between them. This leads me to ask <span style="font-weight:450;">how models can use external knowledge to solve increasingly challenging problems</span>. I believe we already have plenty of knowledge to draw on, especially the knowledge that keeps evolving and accumulating. We need memory systems that models can manage on their own, so they can reuse prior knowledge instead of reasoning from scratch and avoid repeating past failures.
</p>

<p style="color:#000; font-weight:300; font-size:15px; margin-bottom:12px;">
  Retrieving such knowledge is hard with existing methods, since it rarely looks similar on the surface. Still, humans (especially domain experts) intuitively know where to look in a vast search space and find connections that seem obvious only in hindsight, a kind of research taste explored in <a href="{{ '/project/ScholarCatalyst/' | relative_url }}" style="color:#0E8C8C; font-weight:450;">ScholarCatalyst</a>. I aim to build models that find such connections for better decision making in open-ended, long-horizon problems.
</p>

<p style="color:#000; font-weight:300; font-size:15px; margin-bottom:12px;">
  I enjoy thinking and reading about research and beyond. You can find my thoughts on my <a href="{{ '/blog/' | relative_url }}" style="color:#0E8C8C; font-weight:450;">Blog</a> and <a href="{{ '/philosophy/' | relative_url }}" style="color:#0E8C8C; font-weight:450;">Research Philosophy</a>.
</p>
  </div>
</div>

<div style="height:15px;"></div>

<div style="height:45px;"></div>
### Research
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; align-items:center; gap:16px;">
  <a href="https://ai.stanford.edu/blog/scholarcatalyst/" class="scholarcatalyst-figure" style="flex-shrink:0;"><img src="{{ '/assets/img/sail.jpg' | relative_url }}" alt="Stanford AI Lab" style="height:52px; width:auto; max-width:none;"></a>
  <div>
  <a href="https://ai.stanford.edu/blog/scholarcatalyst/" style="color:#000; font-weight:500">Research Intuition as a Retrieval Task</a><br>
  <span style="font-size:0.92em; font-weight:350;"><span style="text-decoration:underline;">Sohyeon Kim</span> and Yoonho Lee</span><br>
  <span style="font-size:15px;">November 2026&nbsp;&nbsp;<a href="https://ai.stanford.edu/blog/scholarcatalyst/" style="color:#0E8C8C; font-weight:450;">SAIL Blog Post</a></span>
  </div>
  </div>
</p>
<p style="margin:0; margin-top:28px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:500">ScholarCatalyst: A Benchmark for Retrieving Papers that Inspire New Research</span>
  </div>
  <span style="font-size:0.92em; font-weight:350;"><span style="text-decoration:underline;">Sohyeon Kim</span><sup>*</sup>, Yoonho Lee<sup>*</sup>, Bo Liu, Dayoon Ko, Rulin Shao, Seungone Kim, Graham Neubig, Pang Wei Koh, Aakanksha Chowdhery, Akari Asai, Omar Khattab, Yejin Choi, Gunhee Kim, Chelsea Finn</span><br>
  <span style="font-size:15px;">Preprint 2026&nbsp;&nbsp;<a href="{{ '/project/ScholarCatalyst/' | relative_url }}" style="color:#0E8C8C; font-weight:450;">Website</a>&nbsp;&nbsp;<a href="https://arxiv.org/abs/2610.02202" style="color:#0E8C8C; font-weight:450;">Paper</a>&nbsp;&nbsp;<a href="https://github.com/stanford-iris-lab/ScholarCatalyst" style="color:#0E8C8C; font-weight:450;">Code</a>&nbsp;&nbsp;<a href="https://huggingface.co/ScholarCatalyst" style="color:#0E8C8C; font-weight:450;">Data</a>&nbsp;&nbsp;<span style="font-size:13px; color:#777;">*equal contribution</span></span><br>
  <span style="font-size:15px; color:#000;">Selected for Laude Institute's <a href="https://www.laude.org/updates/slingshots-four" style="color:#0E8C8C; font-weight:450;">Slingshots // FOUR</a></span>
</p>
<figure class="scholarcatalyst-figure" style="margin:14px 0 52px 0; display:flex; align-items:center; gap:14px;">
  <a href="https://www.laude.org/updates/slingshots-four"><img src="{{ '/assets/img/scholarcatalyst.png' | relative_url }}" alt="Selected for Laude Institute's Slingshots // FOUR" style="height:200px; width:auto; max-width:none;"></a>
  <a href="{{ '/project/ScholarCatalyst/' | relative_url }}"><img src="{{ '/project/ScholarCatalyst/assets/images/fig1.webp' | relative_url }}" alt="ScholarCatalyst task overview: inspiring papers can be semantically dissimilar while topically related papers may not advance a project." style="height:200px; width:auto; max-width:none;"></a>
</figure>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:500">MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval</span>
  </div>
  <span style="font-size:0.92em; font-weight:350;">Seokwon Song, <span style="text-decoration:underline;">Sohyeon Kim</span>, Gunhee Kim</span><br>
  <span style="font-size:15px;">EMNLP 2026&nbsp;&nbsp;<a href="https://arxiv.org/pdf/2608.30949" style="color:#0E8C8C; font-weight:450;">Paper</a></span>
</p>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:500">When Is Enough Not Enough? Illusory Completion in Search Agents</span>
  </div>
  <span style="font-size:0.92em; font-weight:350;">Dayoon Ko, Jihyuk Kim, <span style="text-decoration:underline;">Sohyeon Kim</span>, Haeju Park, Dahyun Lee, Gunhee Kim, Moontae Lee, Kyungjae Lee</span><br>
  <span style="font-size:15px;"><a href="https://www.aiagentbehavior.com/" style="color:#000;">COLM 2026 Workshop on Agent Behavior</a>&nbsp;&nbsp;<a href="https://arxiv.org/pdf/2602.07549" style="color:#0E8C8C; font-weight:450;">Paper</a></span>
</p>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:500">Hybrid Deep Searcher: Scalable Parallel and Sequential Search Reasoning</span>
  </div>
  <span style="font-size:0.92em; font-weight:350;">Dayoon Ko, Jihyuk Kim, Haeju Park, <span style="text-decoration:underline;">Sohyeon Kim</span>, Dahyun Lee, Yongrae Jo, Gunhee Kim, Moontae Lee, Kyungjae Lee</span><br>
  <span style="font-size:15px;">ICLR 2026&nbsp;&nbsp;<a href="https://openreview.net/pdf?id=rXpTZyucal" style="color:#0E8C8C; font-weight:450;">Paper</a>&nbsp;&nbsp;<a href="https://hybriddeepsearcher.github.io/" style="color:#0E8C8C; font-weight:450;">Website</a></span>
</p>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:500">When Should Dense Retrievers Be Updated in Evolving Corpora? Detecting Out-of-Distribution Corpora Using GradNormIR</span>
  </div>
  <span style="font-size:0.92em; font-weight:350;">Dayoon Ko, Jinyoung Kim, <span style="text-decoration:underline;">Sohyeon Kim</span>, Jinhyuk Kim, Jaehoon Lee, Seonghak Song, Minyoung Lee, Gunhee Kim</span><br>
  <span style="font-size:15px;">ACL 2025 Findings&nbsp;&nbsp;<a href="https://arxiv.org/abs/2506.01877" style="color:#0E8C8C; font-weight:450;">Paper</a></span>
</p>
<div style="height:15px;"></div>

