---
layout: default
---
<div style="height:15px;"></div>
<p style="color:#000; font-weight:300; margin-bottom:12px;"> I am a visiting researcher at <a href="https://irislab.stanford.edu/" style="color:#7A005E;">Stanford University</a>, working with Prof. <a href="https://ai.stanford.edu/~cbfinn/" style="color:#7A005E;">Chelsea Finn</a>. I am also a second-year PhD student at <a href="https://www.snu.ac.kr/" style="color:#7A005E;">Seoul National University</a>, advised by Prof. <a href="https://vision.snu.ac.kr/gunhee/" style="color:#7A005E;">Gunhee Kim</a>.</p>

<p style="color:#000; font-weight:300; margin-bottom:12px;">
  I have always been drawn to what I know, what I do not, and how to explore the gap between them. This leads me to ask <span style="font-weight:400;">how models can use external knowledge to solve increasingly challenging problems</span>. I believe we already have plenty of knowledge to draw on, especially the knowledge that keeps evolving and accumulating. We need memory systems that models can manage on their own, so they can reuse prior knowledge instead of reasoning from scratch and avoid repeating past failures.
</p>

<p style="color:#000; font-weight:300; margin-bottom:12px;">
  Such knowledge is hard to retrieve with existing methods, since it rarely looks similar on the surface. Still, humans (especially domain experts) intuitively know where to look in a vast search space and find connections that seem obvious only in hindsight, a kind of research taste explored in <a href="{{ '/project/ScholarCatalyst/' | relative_url }}" style="color:#7A005E;">ScholarCatalyst</a>. I aim to build models that find such connections for better decision making in open-ended, long-horizon problems.
</p>

<p style="color:#000; font-weight:300; margin-bottom:12px;">
  To learn more about how I think beyond research, read my <a href="{{ '/blog/' | relative_url }}" style="color:#7A005E;">Blog</a>.
</p>

<div style="height:15px;"></div>

<div style="height:45px;"></div>
### Publication
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:400">ScholarCatalyst: A Benchmark for Retrieving Papers that Inspire New Research</span>
  </div>
  <span style="font-size:0.95em;"><span style="font-weight:400; color:#000">Sohyeon Kim</span><sup>*</sup>, Yoonho Lee<sup>*</sup>, Bo Liu, Dayoon Ko, Rulin Shao, Seungone Kim, Graham Neubig, Pang Wei Koh, Aakanksha Chowdhery, Akari Asai, Omar Khattab, Yejin Choi, Gunhee Kim, Chelsea Finn</span><br>
  <span style="font-size:15px;">Preprint 2026&nbsp;&nbsp;<a href="{{ '/project/ScholarCatalyst/' | relative_url }}" style="color:#7A005E;">Website</a>&nbsp;&nbsp;<a href="https://arxiv.org/abs/2610.02202" style="color:#7A005E;">Paper</a>&nbsp;&nbsp;<a href="https://github.com/stanford-iris-lab/ScholarCatalyst" style="color:#7A005E;">Code</a>&nbsp;&nbsp;<a href="https://huggingface.co/ScholarCatalyst" style="color:#7A005E;">Data</a>&nbsp;&nbsp;<span style="font-size:13px; color:#777;">*equal contribution</span></span>
</p>
<figure style="margin:14px 0 52px 0; width:100%;">
  <a href="{{ '/project/ScholarCatalyst/' | relative_url }}"><img src="{{ '/project/ScholarCatalyst/assets/images/fig1.webp' | relative_url }}" alt="ScholarCatalyst task overview: inspiring papers can be semantically dissimilar while topically related papers may not advance a project." style="width:100%; max-width:100%; display:block;"></a>
  <figcaption style="margin-top:8px; font-size:13px; font-weight:300; color:#444;">ScholarCatalyst is a benchmark built from AI researchers’ firsthand accounts of what inspired their work. A paper that inspires a project may share little surface similarity with the question (right), while topically related work may not (left). Even strong retrieval systems, including agents, find only about half of such papers.</figcaption>
</figure>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:400">MULTI3IR: A Benchmark for Multi-perspective Multi-domain Multi-modal Information Retrieval</span>
  </div>
  <span style="font-size:0.95em;">Seokwon Song, <span style="font-weight:400; color:#000">Sohyeon Kim</span>, Gunhee Kim</span><br>
  <span style="font-size:15px;">EMNLP 2026&nbsp;&nbsp;<a href="https://arxiv.org/pdf/2608.30949" style="color:#7A005E;">Paper</a></span>
</p>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:400">When Is Enough Not Enough? Illusory Completion in Search Agents</span>
  </div>
  <span style="font-size:0.95em;">Dayoon Ko, Jihyuk Kim, <span style="font-weight:400; color:#000">Sohyeon Kim</span>, Haeju Park, Dahyun Lee, Gunhee Kim, Moontae Lee, Kyungjae Lee</span><br>
  <span style="font-size:15px;"><a href="https://www.aiagentbehavior.com/" style="color:#000;">COLM 2026 Workshop on Agent Behavior</a>&nbsp;&nbsp;<a href="https://arxiv.org/pdf/2602.07549" style="color:#7A005E;">Paper</a></span>
</p>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:400">Hybrid Deep Searcher: Scalable Parallel and Sequential Search Reasoning</span>
  </div>
  <span style="font-size:0.95em;">Dayoon Ko, Jihyuk Kim, Haeju Park, <span style="font-weight:400; color:#000">Sohyeon Kim</span>, Dahyun Lee, Yongrae Jo, Gunhee Kim, Moontae Lee, Kyungjae Lee</span><br>
  <span style="font-size:15px;">ICLR 2026&nbsp;&nbsp;<a href="https://openreview.net/pdf?id=rXpTZyucal" style="color:#7A005E;">Paper</a>&nbsp;&nbsp;<a href="https://hybriddeepsearcher.github.io/" style="color:#7A005E;">Website</a></span>
</p>
<p style="margin:0; margin-top:10px; font-weight:300">
  <div style="display:flex; justify-content:space-between">
  <span style="color:#000; font-weight:400">When Should Dense Retrievers Be Updated in Evolving Corpora? Detecting Out-of-Distribution Corpora Using GradNormIR</span>
  </div>
  <span style="font-size:0.95em;">Dayoon Ko, Jinyoung Kim, <span style="font-weight:400; color:#000">Sohyeon Kim</span>, Jinhyuk Kim, Jaehoon Lee, Seonghak Song, Minyoung Lee, Gunhee Kim</span><br>
  <span style="font-size:15px;">ACL 2025 Findings&nbsp;&nbsp;<a href="https://arxiv.org/abs/2506.01877" style="color:#7A005E;">Paper</a></span>
</p>
<div style="height:15px;"></div>

