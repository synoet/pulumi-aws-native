// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs } from "../types";
import * as utilities from "../utilities";

/**
 * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html
 */
export class LocationNFS extends pulumi.CustomResource {
    /**
     * Get an existing LocationNFS resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): LocationNFS {
        return new LocationNFS(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:datasync:LocationNFS';

    /**
     * Returns true if the given object is an instance of LocationNFS.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is LocationNFS {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === LocationNFS.__pulumiType;
    }

    public /*out*/ readonly locationArn!: pulumi.Output<string>;
    public /*out*/ readonly locationUri!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions
     */
    public readonly mountOptions!: pulumi.Output<outputs.datasync.LocationNFSMountOptions | undefined>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig
     */
    public readonly onPremConfig!: pulumi.Output<outputs.datasync.LocationNFSOnPremConfig>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname
     */
    public readonly serverHostname!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory
     */
    public readonly subdirectory!: pulumi.Output<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags
     */
    public readonly tags!: pulumi.Output<outputs.Tag[] | undefined>;

    /**
     * Create a LocationNFS resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: LocationNFSArgs, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.onPremConfig === undefined) && !opts.urn) {
                throw new Error("Missing required property 'onPremConfig'");
            }
            if ((!args || args.serverHostname === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverHostname'");
            }
            if ((!args || args.subdirectory === undefined) && !opts.urn) {
                throw new Error("Missing required property 'subdirectory'");
            }
            inputs["mountOptions"] = args ? args.mountOptions : undefined;
            inputs["onPremConfig"] = args ? args.onPremConfig : undefined;
            inputs["serverHostname"] = args ? args.serverHostname : undefined;
            inputs["subdirectory"] = args ? args.subdirectory : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["locationArn"] = undefined /*out*/;
            inputs["locationUri"] = undefined /*out*/;
        } else {
            inputs["locationArn"] = undefined /*out*/;
            inputs["locationUri"] = undefined /*out*/;
            inputs["mountOptions"] = undefined /*out*/;
            inputs["onPremConfig"] = undefined /*out*/;
            inputs["serverHostname"] = undefined /*out*/;
            inputs["subdirectory"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(LocationNFS.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a LocationNFS resource.
 */
export interface LocationNFSArgs {
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-mountoptions
     */
    mountOptions?: pulumi.Input<inputs.datasync.LocationNFSMountOptionsArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-onpremconfig
     */
    onPremConfig: pulumi.Input<inputs.datasync.LocationNFSOnPremConfigArgs>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-serverhostname
     */
    serverHostname: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-subdirectory
     */
    subdirectory: pulumi.Input<string>;
    /**
     * http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-datasync-locationnfs.html#cfn-datasync-locationnfs-tags
     */
    tags?: pulumi.Input<pulumi.Input<inputs.TagArgs>[]>;
}
