# Observations from the supplied TMC corpus

## Provenance and limits

Prepared 2026-10-25 from the user's `tmc_paper/paper` folder. There are **36 readable PDFs and 568 PDF pages**. The [inventory](tmc-corpus-inventory.json) records relative filenames, SHA-256 hashes, page counts, front-matter DOI candidates, keyword tags and candidate headings/caption numbers. The inventory contains no full-paper text or figures. The source PDFs remain in the user's library and are not redistributed in this bundle.

All 36 files were processed for metadata and structure. Selected relevant methods/evaluation pages and three page images were inspected to derive the focused examples below. This does **not** mean all 568 pages or all proofs were reviewed. Automated tags are overlapping title-keyword matches; heading/caption detectors miss split lines and can capture non-headings. The inventory's counts are not manually verified figure totals or a bibliometric survey.

The collection strongly emphasizes FL and edge learning. It also contains security, semantic communication, recommendation, industrial networks, UAV and satellite settings. Its selection cannot establish what TMC universally prefers. DOI year, early-publication date and issue year may differ. DOI candidates are locally extracted, not publisher-verified citations.

## What changes the writing decisions

### 1. Make the operating constraint part of the mechanism

Device capability, time-varying data, communication contact, battery condition or topology often changes how training is scheduled or aggregated. Describe that coupling, not just an application label attached to a generic learning method.

- **TMC05, AdaCLP, PDF p. 8, Sec. V-A:** the setup reports mobile/embedded devices and a larger simulated heterogeneous client population, defines temporal class-imbalance settings, and lists training-time/idle-time/energy-related metrics. **Use:** distinguish measured devices from simulated scale, and operationalize temporal heterogeneity rather than saying only 'non-IID.'
- **TMC20, FL in Motion, PDF p. 11, Sec. VI-A:** the evaluation defines a road, zones, vehicle trajectories generated with SUMO and task/model choices. **Use:** connect mobility-aware selection to a reproducible contact/trajectory setting; do not present a traffic simulation as a field deployment.
- **TMC22, HierTFL, PDF pp. 9-10, Sec. V:** evaluation separates environment description and configuration, with FL tasks and TSN/training parameters. **Use:** explain deadline and network scheduling assumptions alongside model performance when the application is time critical.

### 2. Keep implementation, simulation, and scale separate

- **TMC33, SPFERE, PDF p. 12, Sec. VI-A:** explicitly distinguishes a real-device testbed from a simulation platform, explains their different evaluation roles, and lists heterogeneous devices/network conditions. The page image was checked. **Use:** a small physical testbed and a larger simulator can support different parts of the story. Neither should be relabelled as the other.
- **TMC12, Fed-RAA, PDF p. 8, Sec. VI-A:** describes a multi-threaded PyTorch simulation with 100 clients and capability/bandwidth levels, followed by datasets and model splitting. **Use:** report the simulation architecture and resource generator instead of implying 100 physical clients.
- **TMC27, Parallel Collaborative ADMM, PDF p. 12, Sec. V:** describes hardware and organizes precision/MSE evaluation together with acceleration and an application example. **Use:** report numerical utility and hardware acceleration costs separately; a speedup claim needs its implementation/comparison context.

### 3. PEFT/LLM work needs resource and adaptation context

- **TMC08, FedPipe, PDF p. 8, Sec. IV:** reports LLM/task setup following an adapter aggregation/deployment explanation and Fig. 12. The page image was checked. **PDF p. 9** describes hardware, constrained memory heterogeneity, ranks and synchronization. **PDF p. 10, Fig. 15 and footnote 3** reports convergence using training rounds. **Use:** describe rank/resource adaptation and aggregation compatibility; do not automatically reinterpret round-based convergence as measured wall-clock acceleration. Published prose and parameter counts still require independent checking before reuse.
- **TMC09, ConvertNet, PDF p. 12, Figs. 11-13:** places runtime breakdown, inference-latency stability during retraining and design-choice ablations on one page, with accompanying memory-overhead discussion. The page image was checked. **Use:** a systems narrative can explain where cost occurs, what competing workload is protected, and why a design choice matters.

### 4. Organize evaluation around questions and costs

- **TMC25, KAFL-HD, PDF p. 9, Sec. V-A:** evaluation introduces accuracy, convergence speed, fairness and overhead, then datasets, heterogeneity settings, models and baselines. **Use:** define fairness and the system cost actually measured; do not leave them as abstract adjectives.
- **TMC35, Hat-DFed, PDF p. 10, Sec. VI:** states research questions for model/energy performance, topology sparsity, scale, hyperparameters and components. **Use:** choose experiments that answer the paper's mechanism and boundary questions instead of listing figures in numerical order. This is an adaptable pattern, not a requirement for five RQs.
- **TMC34, Orthogonal Regularization, PDF p. 9, Sec. VI-A:** describes time-series datasets from mobile-relevant tasks including activity recognition and IoT diagnosis. **Use:** a learning-method paper can establish application relevance through its actual workload and failure mode; relevance still needs evidence beyond the dataset name.

### 5. Match theory and security evidence to the stated model

- **TMC32, Spectral-Convergent DML, PDF pp. 7-8, Sec. V:** numerical results specify a simulated constellation, link-success model, EuroSAT learning task and controlled spectral-matrix experiments. **Use:** connect the theoretical quantity to a controlled validation and the network application, keeping both model assumptions and simulation status visible.
- **TMC28, PEFL, PDF p. 13, Sec. VII:** evaluation states that it tests backdoor/collusion resistance and global-model accuracy, then gives the experimental setup. **Use:** report the adversary, attack metric, benign utility and overhead for the particular threat. Keeping training data local alone is a different claim.

## Resulting defaults, with explicit boundaries

- Build the argument as `mobile setting -> constraint/failure -> mechanism -> evidence -> limits`.
- Select architecture for systems, optimization, learning-method, or security contributions; do not mandate a theorem or testbed for all work.
- Put resources, timelines, data partitions, and information assumptions in the model/setup when they affect the mechanism.
- Match efficiency to its actual metric and accounting boundary. Show overhead and fair budgets when needed to support the main claim.
- Use ablations and sensitivities to test the proposed mechanism or operating boundary; do not copy every sweep from another paper.
- Do not turn article lengths, figure counts, recurring headings or sample parameter values into submission rules.

## Source catalog

IDs below are for this fixed inventory and may change when a regenerated corpus gains files. PDF page anchors above refer to one-based pages of the supplied file, not printed journal pages. Search the source filename in the original corpus when following an anchor.

| ID | Source filename (without .pdf) | PDF pages |
|---|---|---:|
| TMC01 | A Federated Recommendation System Framework Based on Variational Autoencoder With Mixture of Experts | 14 |
| TMC02 | A Model Consistency-Based Countermeasure to GAN-Based Data Poisoning Attack in Federated Learning | 19 |
| TMC03 | A Secure and Efficient Distributed Semantic Communication System for Heterogeneous Internet of Things | 15 |
| TMC04 | A Sustainable Incentive Mechanism for Long-Term Cross-Device Federated Learning With Energy Limits and Fairness | 18 |
| TMC05 | AdaCLP Efficient Federated Learning for Asynchronous Mobile Devices With Temporally Imbalanced Data | 17 |
| TMC06 | Adaptive Quantization and Differential Privacy Federated Learning Framework | 16 |
| TMC07 | An Incentive Assignment Scheme of UAV Clients for Federated Intelligent Inspection Based on Communication-Sensing-Computing Integration | 15 |
| TMC08 | Automated Federated Pipeline for Parameter-Efficient Fine-Tuning of Large Language Models | 16 |
| TMC09 | ConvertNet Training-Time Model Scaling for In-Vehicle Continuous Learning | 17 |
| TMC10 | Delay-Trajectory-Accuracy Trilemma Optimization for Non-IID Mitigation in AAV-Cooperative Federated Learning IoT | 18 |
| TMC11 | Energy and Memory-Efficient Federated Learning With Ordered Layer Freezing | 15 |
| TMC12 | Fed-RAA Resource-Adaptive Asynchronous Federated Edge Learning With Theoretical Guarantee | 14 |
| TMC13 | Federated Chain Context Optimization for Long-Tailed Multi-Label Image Classification | 12 |
| TMC14 | Federated Linear Bandit Learning via UAV Aided Over-the-Air Computation | 16 |
| TMC15 | Federated Unlearning via Distilled Data | 12 |
| TMC16 | FedGSE Gradient-Based Submodel Extraction for Resource-Constrained Federated Learning | 13 |
| TMC17 | FedHRA A Joint Optimization Framework for Fast Convergent Decentralized Federated Learning in LEO Satellite Networks | 14 |
| TMC18 | FedMeld A Model-Dispersal Federated Learning Framework for Space-Ground Integrated Networks | 14 |
| TMC19 | FedShieldLLM Measurement- Detection and Protection of Privacy Leakage in Federated LLMs | 17 |
| TMC20 | FL in Motion Accelerating FL via Mobility-Aware Vehicle Selection and Sparse Training | 15 |
| TMC21 | Heterogeneity-Aware Semi-Supervised Federated Learning With Client-to-Client Collaboration | 18 |
| TMC22 | HierTFL Hierarchical Scheduling for Industrial TSN-Enhanced Federated Learning System | 15 |
| TMC23 | IRS Aided Federated Learning Multiple Access and Fundamental Tradeoff | 18 |
| TMC24 | Joint UAV 3D Deployment and Ground Device Association Optimizing for Multi-UAV-Aided MEC Heterogeneous Network | 16 |
| TMC25 | KAFL-HD Knowledge Alignment in Asynchronous Federated Learning With Heterogeneous Data | 16 |
| TMC26 | Navigating Federated Semi-Supervised Learning in Dual Data Heterogeneity | 14 |
| TMC27 | Parallel Collaborative ADMM Privacy Computing and Adaptive GPU Acceleration for Distributed Edge Networks | 18 |
| TMC28 | PEFL A Privacy-Enhanced Federated Learning Framework for Mobile Edge CrowdSensing in the Presence of Collusion and Backdoor Attacks | 17 |
| TMC29 | Representation Optimal Matching for Federated Learning With Noisy Labels in Remote Sensing | 17 |
| TMC30 | SMTFL Secure Model Training to Untrusted Participants in Federated Learning | 17 |
| TMC31 | Soft-Label Caching and Sharpening for Communication-Efficient Federated Distillation | 17 |
| TMC32 | Spectral-Convergent Decentralized Machine Learning Theory and Application in Space Networks | 12 |
| TMC33 | SPFERE Toward Practical Semi-Synchronous On-Device Federated Edge Learning With Fairness and Power Awareness | 18 |
| TMC34 | Tackling Spatial-Temporal Heterogeneous Federated Learning With Orthogonal Regularization | 17 |
| TMC35 | Towards Heterogeneity-Aware and Energy-Efficient Topology Optimization for Decentralized Federated Learning in Edge Environment | 16 |
| TMC36 | Trust Management Based on Attention-Weighted Federated Deep Reinforcement Learning for Underwater Acoustic Sensor Networks | 15 |
