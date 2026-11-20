(() => {
  "use strict";
  const $ = (selector, root = document) => root.querySelector(selector);
  const $$ = (selector, root = document) => [...root.querySelectorAll(selector)];

  const menu = $("#menu");
  const menuToggle = $("#menuToggle");
  menuToggle?.addEventListener("click", () => {
    const open = menu.classList.toggle("open");
    menuToggle.setAttribute("aria-expanded", String(open));
    menuToggle.textContent = open ? "Close" : "Menu";
  });
  $$("#menu a").forEach((link) => link.addEventListener("click", () => {
    menu.classList.remove("open");
    menuToggle?.setAttribute("aria-expanded", "false");
    if (menuToggle) menuToggle.textContent = "Menu";
  }));

  const revealItems = $$('[data-reveal]');
  if ("IntersectionObserver" in window) {
    const observer = new IntersectionObserver((entries) => entries.forEach((entry) => {
      if (entry.isIntersecting) { entry.target.classList.add("shown"); observer.unobserve(entry.target); }
    }), { threshold: 0.12 });
    revealItems.forEach((item) => observer.observe(item));
  } else revealItems.forEach((item) => item.classList.add("shown"));

  const projectData = JSON.parse($("#projectData")?.textContent || "[]");
  const dialog = $("#caseDialog");
  const content = $("#caseContent");
  const escape = (value) => String(value).replace(/[&<>"']/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character]));
  const list = (items, tag = "ul", className = "") => `<${tag}${className ? ` class="${className}"` : ""}>${items.map((item) => `<li>${escape(item)}</li>`).join("")}</${tag}>`;

  $$(".project-open").forEach((button) => button.addEventListener("click", () => {
    const project = projectData.find((item) => item.slug === button.dataset.project);
    if (!project || !dialog || !content) return;
    content.innerHTML = `<article class="case-content ${escape(project.accent)}">
      <p class="case-kicker">Project case study</p><h2 id="caseTitle">${escape(project.name)}</h2>
      <p class="project-subtitle">${escape(project.subtitle)}</p><p class="case-role"><strong>My involvement:</strong> ${escape(project.role)}</p>
      <div class="case-layout"><div><h3>The problem</h3><p>${escape(project.problem)}</p><h3>The solution</h3><p>${escape(project.solution)}</p></div>
      <div><h3>Key capabilities</h3>${list(project.features)}<h3>Development process</h3>${list(project.process, "ol")}</div></div>
      <h3>Technologies and focus</h3>${list(project.tech, "ul", "case-tags")}<p class="case-status"><strong>Current status:</strong> ${escape(project.status)}</p></article>`;
    dialog.showModal();
  }));
  $(".dialog-close")?.addEventListener("click", () => dialog?.close());
  dialog?.addEventListener("click", (event) => { if (event.target === dialog) dialog.close(); });

  const form = $("#contactForm");
  form?.addEventListener("submit", async (event) => {
    event.preventDefault();
    const status = $("#formStatus");
    const button = $("button[type=submit]", form);
    const formData = new FormData(form);
    const payload = Object.fromEntries(formData.entries());
    if (!payload.name?.trim() || !payload.message?.trim() || !/^\S+@\S+\.\S+$/.test(payload.email || "")) {
      status.textContent = "Please add your name, a valid email, and a message.";
      return;
    }
    button.disabled = true; status.textContent = "Sending…";
    try {
      const response = await fetch(form.dataset.url, { method: "POST", headers: { "Content-Type": "application/json", "X-CSRFToken": $("meta[name=csrf-token]")?.content || "" }, body: JSON.stringify(payload) });
      const result = await response.json();
      if (!response.ok || !result.ok) throw new Error(result.error || "Unable to send your message.");
      form.reset(); status.textContent = "Message sent. Thank you!";
    } catch (error) { status.textContent = error.message || "Network error. Please try again."; }
    button.disabled = false;
  });
})();
