// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const EC2FleetCapacityReservationOptionsRequestUsageStrategy = {
    UseCapacityReservationsFirst: "use-capacity-reservations-first",
} as const;

export type EC2FleetCapacityReservationOptionsRequestUsageStrategy = (typeof EC2FleetCapacityReservationOptionsRequestUsageStrategy)[keyof typeof EC2FleetCapacityReservationOptionsRequestUsageStrategy];

export const EC2FleetExcessCapacityTerminationPolicy = {
    Termination: "termination",
    NoTermination: "no-termination",
} as const;

export type EC2FleetExcessCapacityTerminationPolicy = (typeof EC2FleetExcessCapacityTerminationPolicy)[keyof typeof EC2FleetExcessCapacityTerminationPolicy];

export const EC2FleetSpotOptionsRequestAllocationStrategy = {
    LowestPrice: "lowestPrice",
    Diversified: "diversified",
    CapacityOptimized: "capacityOptimized",
    CapacityOptimizedPrioritized: "capacityOptimizedPrioritized",
} as const;

export type EC2FleetSpotOptionsRequestAllocationStrategy = (typeof EC2FleetSpotOptionsRequestAllocationStrategy)[keyof typeof EC2FleetSpotOptionsRequestAllocationStrategy];

export const EC2FleetSpotOptionsRequestInstanceInterruptionBehavior = {
    Hibernate: "hibernate",
    Stop: "stop",
    Terminate: "terminate",
} as const;

export type EC2FleetSpotOptionsRequestInstanceInterruptionBehavior = (typeof EC2FleetSpotOptionsRequestInstanceInterruptionBehavior)[keyof typeof EC2FleetSpotOptionsRequestInstanceInterruptionBehavior];

export const EC2FleetTagSpecificationResourceType = {
    ClientVpnEndpoint: "client-vpn-endpoint",
    CustomerGateway: "customer-gateway",
    DedicatedHost: "dedicated-host",
    DhcpOptions: "dhcp-options",
    EgressOnlyInternetGateway: "egress-only-internet-gateway",
    ElasticGpu: "elastic-gpu",
    ElasticIp: "elastic-ip",
    ExportImageTask: "export-image-task",
    ExportInstanceTask: "export-instance-task",
    Fleet: "fleet",
    FpgaImage: "fpga-image",
    HostReservation: "host-reservation",
    Image: "image",
    ImportImageTask: "import-image-task",
    ImportSnapshotTask: "import-snapshot-task",
    Instance: "instance",
    InternetGateway: "internet-gateway",
    KeyPair: "key-pair",
    LaunchTemplate: "launch-template",
    LocalGatewayRouteTableVpcAssociation: "local-gateway-route-table-vpc-association",
    Natgateway: "natgateway",
    NetworkAcl: "network-acl",
    NetworkInsightsAnalysis: "network-insights-analysis",
    NetworkInsightsPath: "network-insights-path",
    NetworkInterface: "network-interface",
    PlacementGroup: "placement-group",
    ReservedInstances: "reserved-instances",
    RouteTable: "route-table",
    SecurityGroup: "security-group",
    Snapshot: "snapshot",
    SpotFleetRequest: "spot-fleet-request",
    SpotInstancesRequest: "spot-instances-request",
    Subnet: "subnet",
    TrafficMirrorFilter: "traffic-mirror-filter",
    TrafficMirrorSession: "traffic-mirror-session",
    TrafficMirrorTarget: "traffic-mirror-target",
    TransitGateway: "transit-gateway",
    TransitGatewayAttachment: "transit-gateway-attachment",
    TransitGatewayConnectPeer: "transit-gateway-connect-peer",
    TransitGatewayMulticastDomain: "transit-gateway-multicast-domain",
    TransitGatewayRouteTable: "transit-gateway-route-table",
    Volume: "volume",
    Vpc: "vpc",
    VpcFlowLog: "vpc-flow-log",
    VpcPeeringConnection: "vpc-peering-connection",
    VpnConnection: "vpn-connection",
    VpnGateway: "vpn-gateway",
} as const;

export type EC2FleetTagSpecificationResourceType = (typeof EC2FleetTagSpecificationResourceType)[keyof typeof EC2FleetTagSpecificationResourceType];

export const EC2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType = {
    OnDemand: "on-demand",
    Spot: "spot",
} as const;

export type EC2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType = (typeof EC2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType)[keyof typeof EC2FleetTargetCapacitySpecificationRequestDefaultTargetCapacityType];

export const EC2FleetType = {
    Maintain: "maintain",
    Request: "request",
    Instant: "instant",
} as const;

export type EC2FleetType = (typeof EC2FleetType)[keyof typeof EC2FleetType];

export const FlowLogLogDestinationType = {
    CloudWatchLogs: "cloud-watch-logs",
    S3: "s3",
} as const;

/**
 * Specifies the type of destination to which the flow log data is to be published. Flow log data can be published to CloudWatch Logs or Amazon S3.
 */
export type FlowLogLogDestinationType = (typeof FlowLogLogDestinationType)[keyof typeof FlowLogLogDestinationType];

export const FlowLogResourceType = {
    NetworkInterface: "NetworkInterface",
    Subnet: "Subnet",
    Vpc: "VPC",
} as const;

/**
 * The type of resource for which to create the flow log. For example, if you specified a VPC ID for the ResourceId property, specify VPC for this property.
 */
export type FlowLogResourceType = (typeof FlowLogResourceType)[keyof typeof FlowLogResourceType];

export const FlowLogTrafficType = {
    Accept: "ACCEPT",
    All: "ALL",
    Reject: "REJECT",
} as const;

/**
 * The type of traffic to log. You can log traffic that the resource accepts or rejects, or all traffic.
 */
export type FlowLogTrafficType = (typeof FlowLogTrafficType)[keyof typeof FlowLogTrafficType];

export const HostAutoPlacement = {
    On: "on",
    Off: "off",
} as const;

/**
 * Indicates whether the host accepts any untargeted instance launches that match its instance type configuration, or if it only accepts Host tenancy instance launches that specify its unique host ID.
 */
export type HostAutoPlacement = (typeof HostAutoPlacement)[keyof typeof HostAutoPlacement];

export const HostRecovery = {
    On: "on",
    Off: "off",
} as const;

/**
 * Indicates whether to enable or disable host recovery for the Dedicated Host. Host recovery is disabled by default.
 */
export type HostRecovery = (typeof HostRecovery)[keyof typeof HostRecovery];

export const NetworkInsightsAnalysisStatus = {
    Running: "running",
    Failed: "failed",
    Succeeded: "succeeded",
} as const;

export type NetworkInsightsAnalysisStatus = (typeof NetworkInsightsAnalysisStatus)[keyof typeof NetworkInsightsAnalysisStatus];

export const NetworkInsightsPathProtocol = {
    Tcp: "tcp",
    Udp: "udp",
} as const;

export type NetworkInsightsPathProtocol = (typeof NetworkInsightsPathProtocol)[keyof typeof NetworkInsightsPathProtocol];

export const PrefixListAddressFamily = {
    IPv4: "IPv4",
    IPv6: "IPv6",
} as const;

/**
 * Ip Version of Prefix List.
 */
export type PrefixListAddressFamily = (typeof PrefixListAddressFamily)[keyof typeof PrefixListAddressFamily];

export const SpotFleetEbsBlockDeviceVolumeType = {
    Gp2: "gp2",
    Gp3: "gp3",
    Io1: "io1",
    Io2: "io2",
    Sc1: "sc1",
    St1: "st1",
    Standard: "standard",
} as const;

export type SpotFleetEbsBlockDeviceVolumeType = (typeof SpotFleetEbsBlockDeviceVolumeType)[keyof typeof SpotFleetEbsBlockDeviceVolumeType];

export const SpotFleetRequestConfigDataAllocationStrategy = {
    CapacityOptimized: "capacityOptimized",
    CapacityOptimizedPrioritized: "capacityOptimizedPrioritized",
    Diversified: "diversified",
    LowestPrice: "lowestPrice",
} as const;

export type SpotFleetRequestConfigDataAllocationStrategy = (typeof SpotFleetRequestConfigDataAllocationStrategy)[keyof typeof SpotFleetRequestConfigDataAllocationStrategy];

export const SpotFleetRequestConfigDataExcessCapacityTerminationPolicy = {
    Default: "Default",
    NoTermination: "NoTermination",
} as const;

export type SpotFleetRequestConfigDataExcessCapacityTerminationPolicy = (typeof SpotFleetRequestConfigDataExcessCapacityTerminationPolicy)[keyof typeof SpotFleetRequestConfigDataExcessCapacityTerminationPolicy];

export const SpotFleetRequestConfigDataInstanceInterruptionBehavior = {
    Hibernate: "hibernate",
    Stop: "stop",
    Terminate: "terminate",
} as const;

export type SpotFleetRequestConfigDataInstanceInterruptionBehavior = (typeof SpotFleetRequestConfigDataInstanceInterruptionBehavior)[keyof typeof SpotFleetRequestConfigDataInstanceInterruptionBehavior];

export const SpotFleetRequestConfigDataType = {
    Maintain: "maintain",
    Request: "request",
} as const;

export type SpotFleetRequestConfigDataType = (typeof SpotFleetRequestConfigDataType)[keyof typeof SpotFleetRequestConfigDataType];

export const SpotFleetSpotCapacityRebalanceReplacementStrategy = {
    Launch: "launch",
} as const;

export type SpotFleetSpotCapacityRebalanceReplacementStrategy = (typeof SpotFleetSpotCapacityRebalanceReplacementStrategy)[keyof typeof SpotFleetSpotCapacityRebalanceReplacementStrategy];

export const SpotFleetSpotPlacementTenancy = {
    Dedicated: "dedicated",
    Default: "default",
    Host: "host",
} as const;

export type SpotFleetSpotPlacementTenancy = (typeof SpotFleetSpotPlacementTenancy)[keyof typeof SpotFleetSpotPlacementTenancy];

export const SpotFleetTagSpecificationResourceType = {
    ClientVpnEndpoint: "client-vpn-endpoint",
    CustomerGateway: "customer-gateway",
    DedicatedHost: "dedicated-host",
    DhcpOptions: "dhcp-options",
    EgressOnlyInternetGateway: "egress-only-internet-gateway",
    ElasticGpu: "elastic-gpu",
    ElasticIp: "elastic-ip",
    ExportImageTask: "export-image-task",
    ExportInstanceTask: "export-instance-task",
    Fleet: "fleet",
    FpgaImage: "fpga-image",
    HostReservation: "host-reservation",
    Image: "image",
    ImportImageTask: "import-image-task",
    ImportSnapshotTask: "import-snapshot-task",
    Instance: "instance",
    InternetGateway: "internet-gateway",
    KeyPair: "key-pair",
    LaunchTemplate: "launch-template",
    LocalGatewayRouteTableVpcAssociation: "local-gateway-route-table-vpc-association",
    Natgateway: "natgateway",
    NetworkAcl: "network-acl",
    NetworkInsightsAnalysis: "network-insights-analysis",
    NetworkInsightsPath: "network-insights-path",
    NetworkInterface: "network-interface",
    PlacementGroup: "placement-group",
    ReservedInstances: "reserved-instances",
    RouteTable: "route-table",
    SecurityGroup: "security-group",
    Snapshot: "snapshot",
    SpotFleetRequest: "spot-fleet-request",
    SpotInstancesRequest: "spot-instances-request",
    Subnet: "subnet",
    TrafficMirrorFilter: "traffic-mirror-filter",
    TrafficMirrorSession: "traffic-mirror-session",
    TrafficMirrorTarget: "traffic-mirror-target",
    TransitGateway: "transit-gateway",
    TransitGatewayAttachment: "transit-gateway-attachment",
    TransitGatewayConnectPeer: "transit-gateway-connect-peer",
    TransitGatewayMulticastDomain: "transit-gateway-multicast-domain",
    TransitGatewayRouteTable: "transit-gateway-route-table",
    Volume: "volume",
    Vpc: "vpc",
    VpcFlowLog: "vpc-flow-log",
    VpcPeeringConnection: "vpc-peering-connection",
    VpnConnection: "vpn-connection",
    VpnGateway: "vpn-gateway",
} as const;

export type SpotFleetTagSpecificationResourceType = (typeof SpotFleetTagSpecificationResourceType)[keyof typeof SpotFleetTagSpecificationResourceType];
