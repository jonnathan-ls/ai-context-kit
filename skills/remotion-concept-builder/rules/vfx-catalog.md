# VFX Catalog

Import path from compositions: `../../lib/vfx`
Import path from templates: `../lib/vfx`

## Backgrounds
| Name | Key Props | Use |
|------|-----------|-----|
| StarfieldBg | starCount, opacity | Default for dark/space scenes |
| GradientBg | from, to, colors, angle, direction, animated, opacity | Color gradient |
| NoiseBg | — | Organic noise texture |
| ParticleBg | — | Particle animated background |
| SolidBg | color | Flat color fill |

## Camera
| Name | Key Props | Use |
|------|-----------|-----|
| CameraZoomIn | fromScale, toScale, startFrame, duration | Slow push-in |
| CameraPan | direction, distance, startFrame, duration | Horizontal/vertical pan |
| CameraShake | intensity, startFrame, duration | Impact, energy, tension |
| OrbitCamera | radius, speed | 3D scene orbit wrapper |
| KenBurnsEffect | fromScale, toScale, fromX, fromY | Photo-style slow zoom+pan |
| CrashZoom | — | Fast dramatic zoom |
| WhipPan | — | Fast swipe transition |
| FlyThrough | — | Camera fly-through motion |

## Overlays
| Name | Key Props | Use |
|------|-----------|-----|
| FilmGrainOverlay | intensity (0–1) | Cinematic texture — always on |
| VignetteOverlay | intensity (0–1) | Edge darkening — always on |
| ColorGrade | preset, intensity | Color look — wraps children |
| GlowRing | color, size, opacity | Circular glow halo |
| OutlineGlow | color, blur | Outline glow on elements |
| ExposureFlash | intensity, startFrame, duration | Bright flash on peak |
| ScanlineOverlay | opacity | CRT scanline texture |
| HologramEffect | color, flickerSpeed | Sci-fi hologram |
| NeonBorder | color, width | Neon glowing border |
| LensDistortion | strength | Fisheye/barrel distortion |
| Spotlight | x, y, radius, color | Focused spotlight cone |
| ParallaxLayer | — | Depth parallax effect |
| MaskReveal | — | Mask-based reveal |
| BokehOverlay | — | Depth of field bokeh |
| TiltShiftEffect | — | Miniature tilt-shift look |
| ShadowLayer | — | Drop shadow overlay |

## Particles
| Name | Key Props | Use |
|------|-----------|-----|
| FloatingParticles | count, color, size, speed, opacity | Ambient floating particles |
| ParticleExplosion | count, color, startFrame | Burst at peak moment |
| SparkleEffect | count, color | Sparkle/glitter |
| ConfettiEffect | count, colors | Confetti burst |

## Distortion
| Name | Key Props | Use |
|------|-----------|-----|
| GlitchEffect | intensity, frequency | Digital glitch |
| ChromaticAberration | offsetX, offsetY | Color channel shift |
| StrokeDrawOn | — | Stroke draw-on animation |
| HeatDistortion | intensity, speed | Heat shimmer |
| RGBSplitEffect | offset, angle | RGB split / chromatic |
| MotionBlurTrail | strength | Motion blur trail |
| PixelDissolve | progress | Pixel-by-pixel dissolve |

## Intensity Guidance

| intensity | filmGrain | vignette | effects guidance |
|-----------|-----------|----------|-----------------|
| low | 0.05 | 0.3 | backgrounds + grain only |
| medium | 0.10 | 0.5 | add particles or glow |
| high | 0.15 | 0.65 | add camera movement + distortion |
| peak | 0.20 | 0.8 | explosion + flash + full motion |

## Adding new VFX

If a concept needs an effect not in this catalog:
1. Create it in `src/lib/vfx/` with a descriptive name
2. Export from `src/lib/vfx/index.ts`
3. Add entry to this catalog file
4. Reference by name in `concept.ts` effects list

Never create VFX inside a composition file.
