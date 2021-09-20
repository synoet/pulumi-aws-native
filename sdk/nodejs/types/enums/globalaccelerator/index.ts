// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const AcceleratorIpAddressType = {
    Ipv4: "IPV4",
    Ipv6: "IPV6",
} as const;

/**
 * IP Address type.
 */
export type AcceleratorIpAddressType = (typeof AcceleratorIpAddressType)[keyof typeof AcceleratorIpAddressType];

export const EndpointGroupHealthCheckProtocol = {
    Tcp: "TCP",
    Http: "HTTP",
    Https: "HTTPS",
} as const;

/**
 * The protocol that AWS Global Accelerator uses to check the health of endpoints in this endpoint group.
 */
export type EndpointGroupHealthCheckProtocol = (typeof EndpointGroupHealthCheckProtocol)[keyof typeof EndpointGroupHealthCheckProtocol];

export const ListenerClientAffinity = {
    None: "NONE",
    SourceIp: "SOURCE_IP",
} as const;

/**
 * Client affinity lets you direct all requests from a user to the same endpoint.
 */
export type ListenerClientAffinity = (typeof ListenerClientAffinity)[keyof typeof ListenerClientAffinity];

export const ListenerProtocol = {
    Tcp: "TCP",
    Udp: "UDP",
} as const;

/**
 * The protocol for the listener.
 */
export type ListenerProtocol = (typeof ListenerProtocol)[keyof typeof ListenerProtocol];
