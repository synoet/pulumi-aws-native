// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::EFS::FileSystem
 */
export class FileSystem extends pulumi.CustomResource {
    /**
     * Get an existing FileSystem resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): FileSystem {
        return new FileSystem(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:efs:FileSystem';

    /**
     * Returns true if the given object is an instance of FileSystem.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is FileSystem {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === FileSystem.__pulumiType;
    }

    public /*out*/ readonly arn!: pulumi.Output<string>;
    public readonly availabilityZoneName!: pulumi.Output<string | undefined>;
    public readonly backupPolicy!: pulumi.Output<outputs.efs.FileSystemBackupPolicy | undefined>;
    /**
     * Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false
     */
    public readonly bypassPolicyLockoutSafetyCheck!: pulumi.Output<boolean | undefined>;
    public readonly encrypted!: pulumi.Output<boolean | undefined>;
    public /*out*/ readonly fileSystemId!: pulumi.Output<string>;
    public readonly fileSystemPolicy!: pulumi.Output<any | undefined>;
    public readonly fileSystemTags!: pulumi.Output<outputs.efs.FileSystemElasticFileSystemTag[] | undefined>;
    public readonly kmsKeyId!: pulumi.Output<string | undefined>;
    public readonly lifecyclePolicies!: pulumi.Output<outputs.efs.FileSystemLifecyclePolicy[] | undefined>;
    public readonly performanceMode!: pulumi.Output<string | undefined>;
    public readonly provisionedThroughputInMibps!: pulumi.Output<number | undefined>;
    public readonly throughputMode!: pulumi.Output<string | undefined>;

    /**
     * Create a FileSystem resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: FileSystemArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["availabilityZoneName"] = args ? args.availabilityZoneName : undefined;
            resourceInputs["backupPolicy"] = args ? args.backupPolicy : undefined;
            resourceInputs["bypassPolicyLockoutSafetyCheck"] = args ? args.bypassPolicyLockoutSafetyCheck : undefined;
            resourceInputs["encrypted"] = args ? args.encrypted : undefined;
            resourceInputs["fileSystemPolicy"] = args ? args.fileSystemPolicy : undefined;
            resourceInputs["fileSystemTags"] = args ? args.fileSystemTags : undefined;
            resourceInputs["kmsKeyId"] = args ? args.kmsKeyId : undefined;
            resourceInputs["lifecyclePolicies"] = args ? args.lifecyclePolicies : undefined;
            resourceInputs["performanceMode"] = args ? args.performanceMode : undefined;
            resourceInputs["provisionedThroughputInMibps"] = args ? args.provisionedThroughputInMibps : undefined;
            resourceInputs["throughputMode"] = args ? args.throughputMode : undefined;
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["fileSystemId"] = undefined /*out*/;
        } else {
            resourceInputs["arn"] = undefined /*out*/;
            resourceInputs["availabilityZoneName"] = undefined /*out*/;
            resourceInputs["backupPolicy"] = undefined /*out*/;
            resourceInputs["bypassPolicyLockoutSafetyCheck"] = undefined /*out*/;
            resourceInputs["encrypted"] = undefined /*out*/;
            resourceInputs["fileSystemId"] = undefined /*out*/;
            resourceInputs["fileSystemPolicy"] = undefined /*out*/;
            resourceInputs["fileSystemTags"] = undefined /*out*/;
            resourceInputs["kmsKeyId"] = undefined /*out*/;
            resourceInputs["lifecyclePolicies"] = undefined /*out*/;
            resourceInputs["performanceMode"] = undefined /*out*/;
            resourceInputs["provisionedThroughputInMibps"] = undefined /*out*/;
            resourceInputs["throughputMode"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(FileSystem.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a FileSystem resource.
 */
export interface FileSystemArgs {
    availabilityZoneName?: pulumi.Input<string>;
    backupPolicy?: pulumi.Input<inputs.efs.FileSystemBackupPolicyArgs>;
    /**
     * Whether to bypass the FileSystemPolicy lockout safety check. The policy lockout safety check determines whether the policy in the request will prevent the principal making the request to be locked out from making future PutFileSystemPolicy requests on the file system. Set BypassPolicyLockoutSafetyCheck to True only when you intend to prevent the principal that is making the request from making a subsequent PutFileSystemPolicy request on the file system. Defaults to false
     */
    bypassPolicyLockoutSafetyCheck?: pulumi.Input<boolean>;
    encrypted?: pulumi.Input<boolean>;
    fileSystemPolicy?: any;
    fileSystemTags?: pulumi.Input<pulumi.Input<inputs.efs.FileSystemElasticFileSystemTagArgs>[]>;
    kmsKeyId?: pulumi.Input<string>;
    lifecyclePolicies?: pulumi.Input<pulumi.Input<inputs.efs.FileSystemLifecyclePolicyArgs>[]>;
    performanceMode?: pulumi.Input<string>;
    provisionedThroughputInMibps?: pulumi.Input<number>;
    throughputMode?: pulumi.Input<string>;
}
