// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::ElastiCache::ReplicationGroup
 */
export function getReplicationGroup(args: GetReplicationGroupArgs, opts?: pulumi.InvokeOptions): Promise<GetReplicationGroupResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:elasticache:getReplicationGroup", {
        "replicationGroupId": args.replicationGroupId,
    }, opts);
}

export interface GetReplicationGroupArgs {
    replicationGroupId: string;
}

export interface GetReplicationGroupResult {
    readonly authToken?: string;
    readonly autoMinorVersionUpgrade?: boolean;
    readonly automaticFailoverEnabled?: boolean;
    readonly cacheNodeType?: string;
    readonly cacheParameterGroupName?: string;
    readonly cacheSecurityGroupNames?: string[];
    readonly clusterMode?: string;
    readonly configurationEndPointAddress?: string;
    readonly configurationEndPointPort?: string;
    readonly engineVersion?: string;
    readonly ipDiscovery?: string;
    readonly logDeliveryConfigurations?: outputs.elasticache.ReplicationGroupLogDeliveryConfigurationRequest[];
    readonly multiAZEnabled?: boolean;
    readonly nodeGroupConfiguration?: outputs.elasticache.ReplicationGroupNodeGroupConfiguration[];
    readonly notificationTopicArn?: string;
    readonly numCacheClusters?: number;
    readonly numNodeGroups?: number;
    readonly preferredMaintenanceWindow?: string;
    readonly primaryClusterId?: string;
    readonly primaryEndPointAddress?: string;
    readonly primaryEndPointPort?: string;
    readonly readEndPointAddresses?: string;
    readonly readEndPointAddressesList?: string[];
    readonly readEndPointPorts?: string;
    readonly readEndPointPortsList?: string[];
    readonly readerEndPointAddress?: string;
    readonly readerEndPointPort?: string;
    readonly replicationGroupDescription?: string;
    readonly securityGroupIds?: string[];
    readonly snapshotRetentionLimit?: number;
    readonly snapshotWindow?: string;
    readonly snapshottingClusterId?: string;
    readonly tags?: outputs.elasticache.ReplicationGroupTag[];
    readonly transitEncryptionEnabled?: boolean;
    readonly transitEncryptionMode?: string;
    readonly userGroupIds?: string[];
}
/**
 * Resource Type definition for AWS::ElastiCache::ReplicationGroup
 */
export function getReplicationGroupOutput(args: GetReplicationGroupOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetReplicationGroupResult> {
    return pulumi.output(args).apply((a: any) => getReplicationGroup(a, opts))
}

export interface GetReplicationGroupOutputArgs {
    replicationGroupId: pulumi.Input<string>;
}
