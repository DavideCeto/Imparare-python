// LinkedIn carousel generator for "Beginning Python — From Blocks to Code with Monty"
// Generated via the linkedin-carousel-generator skill.
const path = require("path");
const pptxgen = require("pptxgenjs");

const ROOT = path.join(__dirname, "..");
const IMG = (...p) => path.join(ROOT, "docs", "img", ...p);
const SIM = (...p) => path.join(ROOT, "docs", "sims", ...p);
const SLIDE_IMG = (...p) => path.join(__dirname, "slides", ...p);

const pptx = new pptxgen();
pptx.defineLayout({ name: "SQUARE", width: 10, height: 10 });
pptx.layout = "SQUARE";

const C = {
  primary: "642580",
  accent: "41BAC1",
  white: "FFFFFF",
  offWhite: "F7F5FA",
  ink: "212121",
  gray: "6B6B6B",
};
const FONT_TITLE = "Georgia";
const FONT_BODY = "Calibri";

// ---------- Slide patterns ----------

function coverSlide(pptx, { coverImage, headline, subhead, tagline }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addImage({ path: coverImage, x: 0.3, y: 0.4, w: 9.4, h: 4.92, sizing: { type: "contain", w: 9.4, h: 4.92 } });
  s.addShape(pptx.ShapeType.rect, { x: 0, y: 5.5, w: 10, h: 4.5, fill: { color: C.primary } });
  s.addText(headline, {
    x: 0.5, y: 5.8, w: 9, h: 1.1,
    fontFace: FONT_TITLE, fontSize: 40, bold: true, color: C.white, align: "center",
  });
  s.addText(subhead, {
    x: 0.5, y: 6.9, w: 9, h: 0.7,
    fontFace: FONT_BODY, fontSize: 20, italic: true, color: C.accent, align: "center",
  });
  s.addText(tagline, {
    x: 0.6, y: 8.6, w: 8.8, h: 0.9,
    fontFace: FONT_BODY, fontSize: 16, color: C.white, align: "center", valign: "top",
  });
  return s;
}

function mascotAsideSlide(pptx, { heading, body, mascotPath }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addImage({ path: mascotPath, x: 0.5, y: 3.9, w: 2.2, h: 2.2 });
  s.addText(heading, {
    x: 3.1, y: 0.9, w: 6.4, h: 1.2,
    fontFace: FONT_TITLE, fontSize: 32, bold: true, color: C.primary,
  });
  s.addText(body, {
    x: 3.1, y: 2.3, w: 6.4, h: 6.3,
    fontFace: FONT_BODY, fontSize: 19, color: C.ink, valign: "top", lineSpacing: 27,
  });
  return s;
}

function imageAsideSlide(pptx, { heading, body, imagePath, imageSide = "right" }) {
  const s = pptx.addSlide();
  s.background = { color: C.offWhite };
  const textX = imageSide === "right" ? 0.6 : 4.4;
  const imgX = imageSide === "right" ? 5.0 : 0.6;
  s.addText(heading, {
    x: textX, y: 0.7, w: 3.9, h: 1.1,
    fontFace: FONT_TITLE, fontSize: 26, bold: true, color: C.primary,
  });
  s.addText(body, {
    x: textX, y: 1.9, w: 3.9, h: 6.8,
    fontFace: FONT_BODY, fontSize: 16, color: C.ink, valign: "top", lineSpacing: 23,
  });
  s.addImage({ path: imagePath, x: imgX, y: 1.7, w: 4.4, h: 4.4, sizing: { type: "contain", w: 4.4, h: 4.4 } });
  return s;
}

function bigNumbersSlide(pptx, { heading, stats, footer }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.6, w: 8.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 28, bold: true, color: C.primary, align: "center",
  });
  const colW = 8.8 / stats.length;
  stats.forEach((stat, i) => {
    s.addText(stat.number, {
      x: 0.6 + i * colW, y: 2.3, w: colW, h: 1.6,
      fontFace: FONT_TITLE, fontSize: 48, bold: true, color: C.accent, align: "center",
    });
    s.addText(stat.label, {
      x: 0.6 + i * colW, y: 3.9, w: colW, h: 0.8,
      fontFace: FONT_BODY, fontSize: 15, color: C.ink, align: "center",
    });
  });
  if (footer) {
    s.addText(footer, {
      x: 0.9, y: 5.3, w: 8.2, h: 3.8,
      fontFace: FONT_BODY, fontSize: 16, color: C.gray, align: "center", valign: "top", lineSpacing: 24,
    });
  }
  return s;
}

function iconRowSlide(pptx, { heading, items }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.6, w: 8.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 27, bold: true, color: C.primary, align: "center",
  });
  const colW = 8.8 / items.length;
  items.forEach((item, i) => {
    s.addText(item.emoji, {
      x: 0.6 + i * colW, y: 2.6, w: colW, h: 1.2, fontSize: 44, align: "center",
    });
    s.addText(item.label, {
      x: 0.6 + i * colW, y: 4.0, w: colW, h: 0.6,
      fontFace: FONT_BODY, fontSize: 17, bold: true, color: C.primary, align: "center",
    });
    s.addText(item.caption, {
      x: 0.5 + i * colW, y: 4.6, w: colW + 0.2, h: 2.0,
      fontFace: FONT_BODY, fontSize: 13, color: C.gray, align: "center", valign: "top",
    });
  });
  return s;
}

function poseGridSlide(pptx, { heading, poses }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.5, w: 8.8, h: 0.9,
    fontFace: FONT_TITLE, fontSize: 27, bold: true, color: C.primary, align: "center",
  });
  const perRow = 4;
  const cellW = 8.8 / perRow;
  poses.forEach((pose, i) => {
    const col = i % perRow, row = Math.floor(i / perRow);
    const rowCount = row === Math.floor((poses.length - 1) / perRow)
      ? poses.length - row * perRow
      : perRow;
    const rowOffset = (8.8 - rowCount * cellW) / 2;
    const x = 0.6 + rowOffset + col * cellW, y = 1.7 + row * 3.7;
    s.addImage({ path: pose.path, x: x + cellW / 2 - 0.7, y, w: 1.4, h: 1.4 });
    s.addText(pose.role, {
      x: x - 0.15, y: y + 1.5, w: cellW + 0.3, h: 0.8,
      fontFace: FONT_BODY, fontSize: 12, color: C.ink, align: "center",
    });
  });
  return s;
}

function badgeCalloutSlide(pptx, { heading, body, badgePath, emoji }) {
  const s = pptx.addSlide();
  s.background = { color: C.offWhite };
  if (badgePath) {
    s.addImage({ path: badgePath, x: 3.0, y: 1.0, w: 4.0, h: 1.75, sizing: { type: "contain", w: 4.0, h: 1.75 } });
  } else if (emoji) {
    s.addText(emoji, { x: 3.5, y: 0.9, w: 3.0, h: 2.0, fontSize: 80, align: "center" });
  }
  s.addText(heading, {
    x: 0.6, y: 3.4, w: 8.8, h: 0.9,
    fontFace: FONT_TITLE, fontSize: 27, bold: true, color: C.primary, align: "center",
  });
  s.addText(body, {
    x: 1.1, y: 4.4, w: 7.8, h: 4.2,
    fontFace: FONT_BODY, fontSize: 18, color: C.ink, align: "center", valign: "top", lineSpacing: 26,
  });
  return s;
}

function checklistRecapSlide(pptx, { heading, items }) {
  const s = pptx.addSlide();
  s.background = { color: C.white };
  s.addText(heading, {
    x: 0.6, y: 0.6, w: 8.8, h: 1.0,
    fontFace: FONT_TITLE, fontSize: 27, bold: true, color: C.primary, align: "center",
  });
  const rowH = 6.6 / items.length;
  items.forEach((item, i) => {
    const y = 1.9 + i * rowH;
    s.addText("✅", { x: 0.9, y, w: 0.6, h: rowH, fontSize: 22, valign: "middle" });
    s.addText(item, {
      x: 1.6, y, w: 7.4, h: rowH,
      fontFace: FONT_BODY, fontSize: 18, bold: true, color: C.ink, valign: "middle",
    });
  });
  return s;
}

function closingCtaSlide(pptx, { headline, siteUrl, repoUrl, mascotPath }) {
  const s = pptx.addSlide();
  s.background = { color: C.primary };
  s.addImage({ path: mascotPath, x: 4.0, y: 0.8, w: 2.0, h: 2.0 });
  s.addText(headline, {
    x: 0.6, y: 3.2, w: 8.8, h: 1.3,
    fontFace: FONT_TITLE, fontSize: 30, bold: true, color: C.white, align: "center",
  });
  s.addText(siteUrl, {
    x: 0.6, y: 4.9, w: 8.8, h: 0.6,
    fontFace: FONT_BODY, fontSize: 20, bold: true, color: C.accent, align: "center",
  });
  s.addText(repoUrl, {
    x: 0.6, y: 5.6, w: 8.8, h: 0.5,
    fontFace: FONT_BODY, fontSize: 15, color: C.white, align: "center",
  });
  s.addText("450 concepts • 38 chapters • 31 MicroSims • free & open source", {
    x: 0.6, y: 8.5, w: 8.8, h: 0.6,
    fontFace: FONT_BODY, fontSize: 13, italic: true, color: C.white, align: "center",
  });
  return s;
}

// ---------- Build the 13 slides ----------

// 1. Cover
coverSlide(pptx, {
  coverImage: IMG("cover.png"),
  headline: "Beginning Python",
  subhead: "From Blocks to Code with Monty",
  tagline: "An intelligent textbook for ages 10 and up — free, interactive, and open source",
});

// 2. Why This Book
mascotAsideSlide(pptx, {
  heading: "Why This Book",
  body: "Python is the #1 most-taught language in U.S. K-12 schools, yet most beginner resources assume too much. This book is built on a 450-concept learning graph, with every early chapter powered by live Skulpt labs — no installs, no accounts required.",
  mascotPath: IMG("mascot", "thinking.png"),
});

// 3. Learning Graph
imageAsideSlide(pptx, {
  heading: "The Learning Graph",
  body: "450 concepts across 14 taxonomy categories, linked by 838 dependency edges. Foundational ideas sit on the left with no prerequisites; the most advanced topics — like neural networks — sit on the right, reachable only after everything they depend on is mastered.",
  imagePath: SLIDE_IMG("learning-graph-zoom.png"),
  imageSide: "right",
});

// 4. Coverage Summary
bigNumbersSlide(pptx, {
  heading: "38 Chapters, Beginner to Advanced",
  stats: [
    { number: "38", label: "Chapters" },
    { number: "450", label: "Concepts" },
    { number: "1,057", label: "Equivalent Pages" },
  ],
  footer: "Ch 1: Welcome to Python & Skulpt  →  Ch 5: Turtle Graphics  →  Ch 24: Recursion & Fractals  →  Ch 32: Data Viz with Matplotlib  →  Ch 38: Neural Networks & MNIST",
});

// 5. Engagement Strategy
iconRowSlide(pptx, {
  heading: "See It. Run It. Modify It.",
  items: [
    { emoji: "👀", label: "See It", caption: "A short, working turtle program" },
    { emoji: "▶️", label: "Run It", caption: "Click Run, watch Monty draw it live" },
    { emoji: "✏️", label: "Modify It", caption: "Change a color, a shape, a number" },
  ],
});

// 6. Mascot Summary
poseGridSlide(pptx, {
  heading: "Meet Monty, Your Guide",
  poses: [
    { path: IMG("mascot", "welcome.png"), role: "Chapter openings" },
    { path: IMG("mascot", "thinking.png"), role: "Predictions & key ideas" },
    { path: IMG("mascot", "tip.png"), role: "Helpful hints" },
    { path: IMG("mascot", "warning.png"), role: "Spot-the-bug challenges" },
    { path: IMG("mascot", "encouraging.png"), role: "Tough concepts" },
    { path: IMG("mascot", "celebration.png"), role: "Chapter wrap-ups" },
    { path: IMG("mascot", "neutral.png"), role: "General asides" },
  ],
});

// 7. MicroSim Count
imageAsideSlide(pptx, {
  heading: "31 Interactive MicroSims",
  body: "MicroSims are small, playable simulations embedded right in the page — no separate app, no install. This Fractal Tree Explorer lets students drag sliders for branch angle, depth, and shrink, and watch recursion draw itself in real time.",
  imagePath: SIM("fractal-tree-explorer", "fractal-tree-explorer.png"),
  imageSide: "left",
});

// 8. Supplementary Content
iconRowSlide(pptx, {
  heading: "Beyond the Chapters",
  items: [
    { emoji: "📖", label: "338 Terms", caption: "ISO 11179-style glossary" },
    { emoji: "❓", label: "83 Answers", caption: "Frequently asked questions" },
    { emoji: "📝", label: "380 Questions", caption: "Self-check quizzes, every chapter" },
    { emoji: "📚", label: "380 References", caption: "Annotated, curated sources" },
  ],
});

// 9. License
badgeCalloutSlide(pptx, {
  heading: "Open License, Yours to Adapt",
  body: "Free to share, remix, and build on — CC BY-NC-SA 4.0. Swap in your own school's colors, logo, and mascot, as long as you keep it open and give credit.",
  badgePath: IMG("license.png"),
});

// 10. Adaptivity
iconRowSlide(pptx, {
  heading: "Add a New Chapter in an Afternoon",
  items: [
    { emoji: "📋", label: "Describe It", caption: "A short course description" },
    { emoji: "🕸️", label: "Map It", caption: "Concepts slot into the learning graph" },
    { emoji: "✍️", label: "Generate It", caption: "AI skills draft the lesson" },
    { emoji: "📖", label: "Ship It", caption: "Same mascot, same style, same rigor" },
  ],
});

// 11. Continuous Enrichment
badgeCalloutSlide(pptx, {
  heading: "Built to Keep Improving",
  body: "Every page and MicroSim already reports real usage through Google Analytics — the foundation for agents that can propose new content or MicroSim variants and let engagement data help pick the winner.",
  emoji: "📊",
});

// 12. Summary of Benefits
checklistRecapSlide(pptx, {
  heading: "Why Students & Teachers Love It",
  items: [
    "450 concepts, 0 dependency violations",
    "31 interactive MicroSims, playable in-browser",
    "338 glossary terms · 380 quiz questions · 380 references",
    "No installs, no accounts — Skulpt runs in the browser",
    "Free, open source, and yours to customize",
  ],
});

// 13. Closing CTA
closingCtaSlide(pptx, {
  headline: "Ready to Start Coding?",
  siteUrl: "dmccreary.github.io/learning-python",
  repoUrl: "github.com/dmccreary/learning-python",
  mascotPath: IMG("mascot", "celebration.png"),
});

pptx.writeFile({ fileName: path.join(__dirname, "beginning-python-carousel.pptx") }).then((fileName) => {
  console.log("Wrote", fileName);
});
