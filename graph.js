/**
 * Interactive Cytoscape.js Threat Network Graph
 */

let cy = null;
let fullGraphData = null;

document.addEventListener('DOMContentLoaded', () => {
  initGraph();

  // Control button bindings
  document.getElementById('btn-graph-fit')?.addEventListener('click', () => cy?.fit(undefined, 30));
  document.getElementById('btn-graph-layout')?.addEventListener('click', runPhysicsLayout);
  document.getElementById('btn-zoom-in')?.addEventListener('click', () => cy?.zoom(cy.zoom() * 1.25));
  document.getElementById('btn-zoom-out')?.addEventListener('click', () => cy?.zoom(cy.zoom() * 0.8));
  document.getElementById('btn-reset-view')?.addEventListener('click', () => { cy?.reset(); cy?.fit(undefined, 30); });

  // Node search binding
  const searchInput = document.getElementById('graph-search-node');
  if (searchInput) {
    searchInput.addEventListener('input', () => {
      const q = searchInput.value.trim().toLowerCase();
      if (!cy) return;
      if (!q) {
        cy.elements().removeClass('faded highlighted');
        return;
      }
      const matched = cy.nodes().filter(n => {
        const d = n.data();
        return (d.label && d.label.toLowerCase().includes(q)) || (d.id && d.id.toLowerCase().includes(q));
      });
      if (matched.length > 0) {
        cy.elements().addClass('faded');
        matched.removeClass('faded').addClass('highlighted');
        matched.neighborhood().removeClass('faded');
        cy.center(matched);
      }
    });
  }

  // Edge type filter binding
  const edgeFilter = document.getElementById('graph-edge-filter');
  if (edgeFilter) {
    edgeFilter.addEventListener('change', () => {
      const filterVal = edgeFilter.value;
      if (!cy || !fullGraphData) return;

      if (filterVal === 'all') {
        cy.elements().remove();
        cy.add(fullGraphData.nodes);
        cy.add(fullGraphData.edges);
      } else {
        const filteredEdges = fullGraphData.edges.filter(e => e.data.relationship_type === filterVal);
        const activeNodeIds = new Set();
        filteredEdges.forEach(e => {
          activeNodeIds.add(e.data.source);
          activeNodeIds.add(e.data.target);
        });
        const filteredNodes = fullGraphData.nodes.filter(n => activeNodeIds.has(n.data.id));
        cy.elements().remove();
        cy.add(filteredNodes);
        cy.add(filteredEdges);
      }
      runPhysicsLayout();
    });
  }
});

async function initGraph() {
  const container = document.getElementById('cy-container');
  if (!container) return;

  try {
    const res = await fetch('/api/graph/data');
    const result = await res.json();
    if (result.status !== 'success' || !result.data) {
      throw new Error('Invalid graph data');
    }

    fullGraphData = result.data;

    // Cytoscape Instance
    cy = cytoscape({
      container: container,
      elements: {
        nodes: fullGraphData.nodes,
        edges: fullGraphData.edges
      },
      style: [
        {
          selector: 'node',
          style: {
            'label': 'data(label)',
            'color': '#f1f5f9',
            'font-family': 'Inter, sans-serif',
            'font-size': '10px',
            'text-valign': 'bottom',
            'text-margin-y': 6,
            'background-color': '#00f0ff',
            'border-width': 2,
            'border-color': 'rgba(255,255,255,0.4)',
            'width': 28,
            'height': 28,
            'transition-property': 'background-color, border-color, width, height, opacity',
            'transition-duration': '0.2s'
          }
        },
        // Node types styling
        {
          selector: 'node[type = "Threat Actor"]',
          style: {
            'background-color': '#00f0ff',
            'border-color': '#ffffff',
            'width': 36,
            'height': 36,
            'font-size': '11px',
            'font-weight': 'bold'
          }
        },
        {
          selector: 'node[type = "Handle"]',
          style: {
            'background-color': '#38bdf8',
            'border-color': 'rgba(56, 189, 248, 0.4)',
            'width': 24,
            'height': 24
          }
        },
        {
          selector: 'node[type = "PGP Key"]',
          style: {
            'background-color': '#f59e0b',
            'border-color': 'rgba(245, 158, 11, 0.4)',
            'shape': 'diamond',
            'width': 26,
            'height': 26
          }
        },
        {
          selector: 'node[type = "Wallet"]',
          style: {
            'background-color': '#10b981',
            'border-color': 'rgba(16, 185, 129, 0.4)',
            'shape': 'hexagon',
            'width': 26,
            'height': 26
          }
        },
        {
          selector: 'node[type = "Marketplace"]',
          style: {
            'background-color': '#8b5cf6',
            'border-color': 'rgba(139, 92, 246, 0.4)',
            'shape': 'round-rectangle',
            'width': 28,
            'height': 28
          }
        },
        {
          selector: 'node[type = "Infrastructure"]',
          style: {
            'background-color': '#ec4899',
            'border-color': 'rgba(236, 72, 153, 0.4)',
            'shape': 'triangle',
            'width': 26,
            'height': 26
          }
        },
        // Edges styling
        {
          selector: 'edge',
          style: {
            'width': 1.5,
            'line-color': 'rgba(0, 240, 255, 0.25)',
            'target-arrow-color': 'rgba(0, 240, 255, 0.4)',
            'target-arrow-shape': 'triangle',
            'curve-style': 'bezier',
            'arrow-scale': 0.8,
            'transition-property': 'line-color, width, opacity',
            'transition-duration': '0.2s'
          }
        },
        {
          selector: 'edge[relationship_type = "Potential Persona Link"]',
          style: {
            'line-style': 'dashed',
            'line-color': '#ec4899',
            'target-arrow-color': '#ec4899',
            'width': 2
          }
        },
        {
          selector: 'edge[relationship_type = "Trust Relationship"]',
          style: {
            'line-color': '#10b981',
            'target-arrow-color': '#10b981',
            'width': 2.5
          }
        },
        // Highlight states
        {
          selector: '.highlighted',
          style: {
            'border-color': '#ffffff',
            'border-width': 4,
            'shadow-blur': 20,
            'shadow-color': '#00f0ff',
            'shadow-opacity': 0.8
          }
        },
        {
          selector: '.faded',
          style: {
            'opacity': 0.15
          }
        }
      ],
      layout: {
        name: 'cose',
        animate: false,
        padding: 40,
        nodeRepulsion: function( node ){ return 409600; },
        idealEdgeLength: function( edge ){ return 80; }
      }
    });

    // Interaction Handlers
    cy.on('tap', 'node', function(evt) {
      const node = evt.target;
      highlightNeighbors(node);
      showNodeInspector(node.data());
    });

    cy.on('tap', 'edge', function(evt) {
      const edge = evt.target;
      showEdgeInspector(edge.data());
    });

    cy.on('tap', function(evt) {
      if (evt.target === cy) {
        cy.elements().removeClass('faded highlighted');
      }
    });

  } catch (err) {
    console.error('Error initializing graph:', err);
    if (window.showToast) window.showToast('Failed to load relationship graph topology', 'danger');
  }
}

function runPhysicsLayout() {
  if (!cy) return;
  const layout = cy.layout({
    name: 'cose',
    animate: true,
    animationDuration: 800,
    padding: 30,
    nodeRepulsion: function( node ){ return 450000; },
    idealEdgeLength: function( edge ){ return 90; }
  });
  layout.run();
}

function highlightNeighbors(node) {
  cy.elements().addClass('faded');
  node.removeClass('faded').addClass('highlighted');
  node.neighborhood().removeClass('faded');
}

function showNodeInspector(d) {
  const panel = document.getElementById('inspector-content');
  if (!panel) return;

  panel.innerHTML = `
    <div style="background: rgba(0, 240, 255, 0.05); border: 1px solid var(--border-subtle); border-radius: 6px; padding: 12px; margin-bottom: 14px;">
      <div style="font-size: 0.7rem; color: var(--cyber-cyan); text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">Selected Entity Node</div>
      <div style="font-size: 1.05rem; font-weight: 700; color: #fff;">${d.label || d.id}</div>
      <div style="font-size: 0.75rem; color: var(--text-muted);">${d.type} ${d.sublabel ? '• ' + d.sublabel : ''}</div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.8rem; margin-bottom: 16px;">
      ${d.category ? `<div><span style="color: var(--text-muted);">Threat Category:</span> <strong style="color: #fff;">${d.category}</strong></div>` : ''}
      ${d.risk_score !== undefined ? `<div><span style="color: var(--text-muted);">Risk Score:</span> ${window.formatRiskBadge(d.risk_score)}</div>` : ''}
      ${d.confidence !== undefined ? `<div><span style="color: var(--text-muted);">Confidence:</span> <strong class="font-mono" style="color: var(--cyber-cyan);">${d.confidence}%</strong></div>` : ''}
      ${d.currency ? `<div><span style="color: var(--text-muted);">Asset Currency:</span> <strong style="color: var(--cyber-amber);">${d.currency}</strong></div>` : ''}
      ${d.role ? `<div><span style="color: var(--text-muted);">Observed Forum Role:</span> <strong style="color: #fff;">${d.role}</strong></div>` : ''}
      ${d.reputation ? `<div><span style="color: var(--text-muted);">Marketplace Trust Score:</span> <strong style="color: var(--cyber-emerald);">${d.reputation}%</strong></div>` : ''}
    </div>

    ${d.type === 'Threat Actor' ? `
      <a href="/actors/${d.id}" class="btn-cyber" style="width: 100%; justify-content: center;">
        <i class="fa-solid fa-folder-open"></i> Open Full Dossier
      </a>
    ` : ''}
  `;
}

function showEdgeInspector(d) {
  const panel = document.getElementById('inspector-content');
  if (!panel) return;

  panel.innerHTML = `
    <div style="background: rgba(139, 92, 246, 0.08); border: 1px solid rgba(139, 92, 246, 0.3); border-radius: 6px; padding: 12px; margin-bottom: 14px;">
      <div style="font-size: 0.7rem; color: var(--cyber-purple); text-transform: uppercase; font-weight: 700; margin-bottom: 4px;">Attribution Relationship</div>
      <div style="font-size: 0.95rem; font-weight: 700; color: #fff;">${d.relationship_type}</div>
      <div style="font-size: 0.75rem; color: var(--text-muted); font-family: var(--font-mono); margin-top: 4px;">
        ${d.source} ➔ ${d.target}
      </div>
    </div>

    <div style="display: flex; flex-direction: column; gap: 10px; font-size: 0.8rem; margin-bottom: 16px;">
      <div><span style="color: var(--text-muted);">Attribution Confidence:</span> <strong class="font-mono" style="color: var(--cyber-emerald);">${d.confidence}%</strong></div>
      <div style="background: rgba(0,0,0,0.3); padding: 10px; border-radius: 4px; border-left: 2px solid var(--cyber-cyan);">
        <span style="color: var(--text-muted); display: block; font-size: 0.72rem; text-transform: uppercase; margin-bottom: 4px;">Observed Evidence:</span>
        <span style="color: var(--text-primary);">${d.evidence || 'Corroborated through multi-source passive telemetry.'}</span>
      </div>
    </div>
  `;
}
