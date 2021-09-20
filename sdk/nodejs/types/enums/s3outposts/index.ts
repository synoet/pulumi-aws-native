// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***


export const BucketRuleStatus = {
    Enabled: "Enabled",
    Disabled: "Disabled",
} as const;

export type BucketRuleStatus = (typeof BucketRuleStatus)[keyof typeof BucketRuleStatus];

export const EndpointAccessType = {
    CustomerOwnedIp: "CustomerOwnedIp",
    Private: "Private",
} as const;

/**
 * The type of access for the on-premise network connectivity for the Outpost endpoint. To access endpoint from an on-premises network, you must specify the access type and provide the customer owned Ipv4 pool.
 */
export type EndpointAccessType = (typeof EndpointAccessType)[keyof typeof EndpointAccessType];

export const EndpointStatus = {
    Available: "Available",
    Pending: "Pending",
    Deleting: "Deleting",
} as const;

export type EndpointStatus = (typeof EndpointStatus)[keyof typeof EndpointStatus];
