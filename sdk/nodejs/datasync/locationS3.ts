// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::DataSync::LocationS3
 */
export class LocationS3 extends pulumi.CustomResource {
    /**
     * Get an existing LocationS3 resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LocationS3 {
        return new LocationS3(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:datasync:LocationS3';

    /**
     * Returns true if the given object is an instance of LocationS3.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LocationS3 {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LocationS3.__pulumiType;
    }

    /**
     * The Amazon Resource Name (ARN) of the Amazon S3 bucket location.
     */
    public /*out*/ readonly locationArn!: pulumi.Output<string>;
    /**
     * The URL of the S3 location that was described.
     */
    public /*out*/ readonly locationUri!: pulumi.Output<string>;
    /**
     * The Amazon Resource Name (ARN) of the Amazon S3 bucket.
     */
    public readonly s3BucketArn!: pulumi.Output<string | undefined>;
    public readonly s3Config!: pulumi.Output<outputs.datasync.LocationS3s3Config>;
    /**
     * The Amazon S3 storage class you want to store your files in when this location is used as a task destination.
     */
    public readonly s3StorageClass!: pulumi.Output<enums.datasync.LocationS3S3StorageClass | undefined>;
    /**
     * A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
     */
    public readonly subdirectory!: pulumi.Output<string | undefined>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    public readonly tags!: pulumi.Output<outputs.datasync.LocationS3Tag[] | undefined>;

    /**
     * Create a LocationS3 resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LocationS3Args, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.s3Config === undefined) && !opts.urn) {
                throw new Error("Missing required property 's3Config'");
            }
            resourceInputs["s3BucketArn"] = args ? args.s3BucketArn : undefined;
            resourceInputs["s3Config"] = args ? args.s3Config : undefined;
            resourceInputs["s3StorageClass"] = args ? args.s3StorageClass : undefined;
            resourceInputs["subdirectory"] = args ? args.subdirectory : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["locationArn"] = undefined /*out*/;
            resourceInputs["locationUri"] = undefined /*out*/;
        } else {
            resourceInputs["locationArn"] = undefined /*out*/;
            resourceInputs["locationUri"] = undefined /*out*/;
            resourceInputs["s3BucketArn"] = undefined /*out*/;
            resourceInputs["s3Config"] = undefined /*out*/;
            resourceInputs["s3StorageClass"] = undefined /*out*/;
            resourceInputs["subdirectory"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(LocationS3.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a LocationS3 resource.
 */
export interface LocationS3Args {
    /**
     * The Amazon Resource Name (ARN) of the Amazon S3 bucket.
     */
    s3BucketArn?: pulumi.Input<string>;
    s3Config: pulumi.Input<inputs.datasync.LocationS3s3ConfigArgs>;
    /**
     * The Amazon S3 storage class you want to store your files in when this location is used as a task destination.
     */
    s3StorageClass?: pulumi.Input<enums.datasync.LocationS3S3StorageClass>;
    /**
     * A subdirectory in the Amazon S3 bucket. This subdirectory in Amazon S3 is used to read data from the S3 source location or write data to the S3 destination.
     */
    subdirectory?: pulumi.Input<string>;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.datasync.LocationS3TagArgs>[]>;
}
