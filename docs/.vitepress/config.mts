import { defineConfig } from 'vitepress'

const base = process.env.DOCS_BASE ?? '/'

export default defineConfig({
  lang: 'fr-FR',
  title: 'Sofian Ecosystem',
  description: 'Base auditée de reconstruction et de conception de Sofian Ecosystem',
  base,
  cleanUrls: true,
  lastUpdated: false,
  themeConfig: {
    nav: [
      { text: 'Comprendre', link: '/' },
      { text: 'Audits', link: '/audits/catalog' },
      { text: 'Besoins', link: '/needs/README' },
      { text: 'Architecture', link: '/architecture/README' },
      { text: 'Opérations', link: '/operations/session-handoff' }
    ],
    sidebar: [
      {
        text: 'Projet',
        items: [
          { text: 'Accueil', link: '/' },
          { text: 'Charte', link: '/project/charter' },
          { text: 'Scope', link: '/project/scope' },
          { text: 'Mode opératoire', link: '/project/operating-model' },
          { text: 'Roadmap', link: '/project/roadmap' },
          { text: 'Définition de fin', link: '/project/definition-of-done' }
        ]
      },
      {
        text: 'Audits',
        items: [
          { text: 'Catalogue', link: '/audits/catalog' },
          { text: 'Couverture', link: '/audits/coverage' },
          { text: 'Sources', link: '/audits/source-registry' },
          { text: 'Preuves', link: '/audits/evidence-model' },
          { text: 'Timeline', link: '/audits/timeline' },
          { text: 'Filiation des noms', link: '/audits/name-lineage' },
          { text: 'Décisions', link: '/audits/decisions' },
          { text: 'Contradictions', link: '/audits/contradictions' }
        ]
      },
      {
        text: 'Besoins et architecture',
        items: [
          { text: 'Besoins', link: '/needs/README' },
          { text: 'Catalogue des besoins', link: '/needs/catalog' },
          { text: 'Matrice de couverture', link: '/needs/coverage-matrix' },
          { text: 'Architecture', link: '/architecture/README' },
          { text: 'État actuel', link: '/architecture/as-is' },
          { text: 'Cibles candidates', link: '/architecture/target-candidates' },
          { text: 'Cible acceptée', link: '/architecture/target-accepted' },
          { text: 'Transition', link: '/architecture/transition' },
          { text: 'Systèmes', link: '/systems/README' },
          { text: 'Workflows', link: '/workflows/README' }
        ]
      },
      {
        text: 'Opérations',
        items: [
          { text: 'Orchestration', link: '/operations/audit-orchestration' },
          { text: 'Protocole subagents', link: '/operations/subagent-protocol' },
          { text: 'Gates de revue', link: '/operations/review-gates' },
          { text: 'Reprise de session', link: '/operations/session-handoff' },
          { text: 'Confidentialité', link: '/operations/privacy-and-publication' }
        ]
      },
      {
        text: 'Référence',
        items: [
          { text: 'Glossaire', link: '/reference/glossary' },
          { text: 'Routage des skills', link: '/reference/skill-routing' }
        ]
      }
    ],
    search: {
      provider: 'local'
    },
    outline: {
      level: [2, 3],
      label: 'Sur cette page'
    },
    docFooter: {
      prev: 'Page précédente',
      next: 'Page suivante'
    },
    returnToTopLabel: 'Retour en haut',
    sidebarMenuLabel: 'Menu',
    darkModeSwitchLabel: 'Apparence',
    lightModeSwitchTitle: 'Passer au thème clair',
    darkModeSwitchTitle: 'Passer au thème sombre'
  }
})
