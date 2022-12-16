// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * An example resource schema demonstrating some basic constructs and validation rules.
 */
export function getCluster(args: GetClusterArgs, opts?: pulumi.InvokeOptions): Promise<GetClusterResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("aws-native:redshift:getCluster", {
        "clusterIdentifier": args.clusterIdentifier,
    }, opts);
}

export interface GetClusterArgs {
    /**
     * A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account
     */
    clusterIdentifier: string;
}

export interface GetClusterResult {
    /**
     * Major version upgrades can be applied during the maintenance window to the Amazon Redshift engine that is running on the cluster. Default value is True
     */
    readonly allowVersionUpgrade?: boolean;
    /**
     * The value represents how the cluster is configured to use AQUA (Advanced Query Accelerator) after the cluster is restored. Possible values include the following.
     *
     * enabled - Use AQUA if it is available for the current Region and Amazon Redshift node type.
     * disabled - Don't use AQUA.
     * auto - Amazon Redshift determines whether to use AQUA.
     */
    readonly aquaConfigurationStatus?: string;
    /**
     * The number of days that automated snapshots are retained. If the value is 0, automated snapshots are disabled. Default value is 1
     */
    readonly automatedSnapshotRetentionPeriod?: number;
    /**
     * The EC2 Availability Zone (AZ) in which you want Amazon Redshift to provision the cluster. Default: A random, system-chosen Availability Zone in the region that is specified by the endpoint
     */
    readonly availabilityZone?: string;
    /**
     * The option to enable relocation for an Amazon Redshift cluster between Availability Zones after the cluster modification is complete.
     */
    readonly availabilityZoneRelocation?: boolean;
    /**
     * The availability zone relocation status of the cluster
     */
    readonly availabilityZoneRelocationStatus?: string;
    /**
     * A boolean value indicating whether the resize operation is using the classic resize process. If you don't provide this parameter or set the value to false , the resize type is elastic.
     */
    readonly classic?: boolean;
    /**
     * The name of the parameter group to be associated with this cluster.
     */
    readonly clusterParameterGroupName?: string;
    /**
     * A list of security groups to be associated with this cluster.
     */
    readonly clusterSecurityGroups?: string[];
    /**
     * The type of the cluster. When cluster type is specified as single-node, the NumberOfNodes parameter is not required and if multi-node, the NumberOfNodes parameter is required
     */
    readonly clusterType?: string;
    /**
     * The version of the Amazon Redshift engine software that you want to deploy on the cluster.The version selected runs on all the nodes in the cluster.
     */
    readonly clusterVersion?: string;
    /**
     * A boolean indicating whether to enable the deferred maintenance window.
     */
    readonly deferMaintenance?: boolean;
    /**
     * An integer indicating the duration of the maintenance window in days. If you specify a duration, you can't specify an end time. The duration must be 45 days or less.
     */
    readonly deferMaintenanceDuration?: number;
    /**
     * A timestamp indicating end time for the deferred maintenance window. If you specify an end time, you can't specify a duration.
     */
    readonly deferMaintenanceEndTime?: string;
    /**
     * A unique identifier for the deferred maintenance window.
     */
    readonly deferMaintenanceIdentifier?: string;
    /**
     * A timestamp indicating the start time for the deferred maintenance window.
     */
    readonly deferMaintenanceStartTime?: string;
    /**
     * The destination AWS Region that you want to copy snapshots to. Constraints: Must be the name of a valid AWS Region. For more information, see Regions and Endpoints in the Amazon Web Services [https://docs.aws.amazon.com/general/latest/gr/rande.html#redshift_region] General Reference
     */
    readonly destinationRegion?: string;
    /**
     * The Elastic IP (EIP) address for the cluster.
     */
    readonly elasticIp?: string;
    /**
     * If true, the data in the cluster is encrypted at rest.
     */
    readonly encrypted?: boolean;
    readonly endpoint?: outputs.redshift.ClusterEndpoint;
    /**
     * An option that specifies whether to create the cluster with enhanced VPC routing enabled. To create a cluster that uses enhanced VPC routing, the cluster must be in a VPC. For more information, see Enhanced VPC Routing in the Amazon Redshift Cluster Management Guide.
     *
     * If this option is true , enhanced VPC routing is enabled.
     *
     * Default: false
     */
    readonly enhancedVpcRouting?: boolean;
    /**
     * Specifies the name of the HSM client certificate the Amazon Redshift cluster uses to retrieve the data encryption keys stored in an HSM
     */
    readonly hsmClientCertificateIdentifier?: string;
    /**
     * Specifies the name of the HSM configuration that contains the information the Amazon Redshift cluster can use to retrieve and store keys in an HSM.
     */
    readonly hsmConfigurationIdentifier?: string;
    /**
     * A list of AWS Identity and Access Management (IAM) roles that can be used by the cluster to access other AWS services. You must supply the IAM roles in their Amazon Resource Name (ARN) format. You can supply up to 50 IAM roles in a single request
     */
    readonly iamRoles?: string[];
    readonly id?: string;
    /**
     * The AWS Key Management Service (KMS) key ID of the encryption key that you want to use to encrypt data in the cluster.
     */
    readonly kmsKeyId?: string;
    readonly loggingProperties?: outputs.redshift.ClusterLoggingProperties;
    /**
     * The name for the maintenance track that you want to assign for the cluster. This name change is asynchronous. The new track name stays in the PendingModifiedValues for the cluster until the next maintenance window. When the maintenance track changes, the cluster is switched to the latest cluster release available for the maintenance track. At this point, the maintenance track name is applied.
     */
    readonly maintenanceTrackName?: string;
    /**
     * The number of days to retain newly copied snapshots in the destination AWS Region after they are copied from the source AWS Region. If the value is -1, the manual snapshot is retained indefinitely.
     *
     * The value must be either -1 or an integer between 1 and 3,653.
     */
    readonly manualSnapshotRetentionPeriod?: number;
    /**
     * The node type to be provisioned for the cluster.Valid Values: ds2.xlarge | ds2.8xlarge | dc1.large | dc1.8xlarge | dc2.large | dc2.8xlarge | ra3.4xlarge | ra3.16xlarge
     */
    readonly nodeType?: string;
    /**
     * The number of compute nodes in the cluster. This parameter is required when the ClusterType parameter is specified as multi-node.
     */
    readonly numberOfNodes?: number;
    /**
     * The port number on which the cluster accepts incoming connections. The cluster is accessible only via the JDBC and ODBC connection strings
     */
    readonly port?: number;
    /**
     * The weekly time range (in UTC) during which automated cluster maintenance can occur.
     */
    readonly preferredMaintenanceWindow?: string;
    /**
     * If true, the cluster can be accessed from a public network.
     */
    readonly publiclyAccessible?: boolean;
    /**
     * The Redshift operation to be performed. Resource Action supports pause-cluster, resume-cluster APIs
     */
    readonly resourceAction?: string;
    /**
     * The identifier of the database revision. You can retrieve this value from the response to the DescribeClusterDbRevisions request.
     */
    readonly revisionTarget?: string;
    /**
     * A boolean indicating if we want to rotate Encryption Keys.
     */
    readonly rotateEncryptionKey?: boolean;
    /**
     * The name of the snapshot copy grant to use when snapshots of an AWS KMS-encrypted cluster are copied to the destination region.
     */
    readonly snapshotCopyGrantName?: string;
    /**
     * Indicates whether to apply the snapshot retention period to newly copied manual snapshots instead of automated snapshots.
     */
    readonly snapshotCopyManual?: boolean;
    /**
     * The number of days to retain automated snapshots in the destination region after they are copied from the source region. 
     *
     *  Default is 7. 
     *
     *  Constraints: Must be at least 1 and no more than 35.
     */
    readonly snapshotCopyRetentionPeriod?: number;
    /**
     * The list of tags for the cluster parameter group.
     */
    readonly tags?: outputs.redshift.ClusterTag[];
    /**
     * A list of Virtual Private Cloud (VPC) security groups to be associated with the cluster.
     */
    readonly vpcSecurityGroupIds?: string[];
}

export function getClusterOutput(args: GetClusterOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetClusterResult> {
    return pulumi.output(args).apply(a => getCluster(a, opts))
}

export interface GetClusterOutputArgs {
    /**
     * A unique identifier for the cluster. You use this identifier to refer to the cluster for any subsequent cluster operations such as deleting or modifying. All alphabetical characters must be lower case, no hypens at the end, no two consecutive hyphens. Cluster name should be unique for all clusters within an AWS account
     */
    clusterIdentifier: pulumi.Input<string>;
}
