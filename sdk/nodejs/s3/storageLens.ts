// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * The AWS::S3::StorageLens resource is an Amazon S3 resource type that you can use to create Storage Lens configurations.
 */
export class StorageLens extends pulumi.CustomResource {
    /**
     * Get an existing StorageLens resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): StorageLens {
        return new StorageLens(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:s3:StorageLens';

    /**
     * Returns true if the given object is an instance of StorageLens.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is StorageLens {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === StorageLens.__pulumiType;
    }

    public readonly storageLensConfiguration!: pulumi.Output<outputs.s3.StorageLensConfiguration>;
    /**
     * A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.
     */
    public readonly tags!: pulumi.Output<outputs.s3.StorageLensTag[] | undefined>;

    /**
     * Create a StorageLens resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: StorageLensArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.storageLensConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'storageLensConfiguration'");
            }
            inputs["storageLensConfiguration"] = args ? args.storageLensConfiguration : undefined;
            inputs["tags"] = args ? args.tags : undefined;
        } else {
            inputs["storageLensConfiguration"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(StorageLens.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a StorageLens resource.
 */
export interface StorageLensArgs {
    storageLensConfiguration: pulumi.Input<inputs.s3.StorageLensConfigurationArgs>;
    /**
     * A set of tags (key-value pairs) for this Amazon S3 Storage Lens configuration.
     */
    tags?: pulumi.Input<pulumi.Input<inputs.s3.StorageLensTagArgs>[]>;
}
