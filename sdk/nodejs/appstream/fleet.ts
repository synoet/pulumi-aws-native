// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import { input as inputs, output as outputs, enums } from "../types";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::AppStream::Fleet
 *
 * @deprecated Fleet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class Fleet extends pulumi.CustomResource {
    /**
     * Get an existing Fleet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Fleet {
        pulumi.log.warn("Fleet is deprecated: Fleet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new Fleet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:appstream:Fleet';

    /**
     * Returns true if the given object is an instance of Fleet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Fleet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Fleet.__pulumiType;
    }

    public readonly computeCapacity!: pulumi.Output<outputs.appstream.FleetComputeCapacity>;
    public readonly description!: pulumi.Output<string | undefined>;
    public readonly disconnectTimeoutInSeconds!: pulumi.Output<number | undefined>;
    public readonly displayName!: pulumi.Output<string | undefined>;
    public readonly domainJoinInfo!: pulumi.Output<outputs.appstream.FleetDomainJoinInfo | undefined>;
    public readonly enableDefaultInternetAccess!: pulumi.Output<boolean | undefined>;
    public readonly fleetType!: pulumi.Output<string | undefined>;
    public readonly iamRoleArn!: pulumi.Output<string | undefined>;
    public readonly idleDisconnectTimeoutInSeconds!: pulumi.Output<number | undefined>;
    public readonly imageArn!: pulumi.Output<string | undefined>;
    public readonly imageName!: pulumi.Output<string | undefined>;
    public readonly instanceType!: pulumi.Output<string>;
    public readonly maxUserDurationInSeconds!: pulumi.Output<number | undefined>;
    public readonly name!: pulumi.Output<string>;
    public readonly streamView!: pulumi.Output<string | undefined>;
    public readonly tags!: pulumi.Output<outputs.appstream.FleetTag[] | undefined>;
    public readonly vpcConfig!: pulumi.Output<outputs.appstream.FleetVpcConfig | undefined>;

    /**
     * Create a Fleet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated Fleet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: FleetArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("Fleet is deprecated: Fleet is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let inputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.computeCapacity === undefined) && !opts.urn) {
                throw new Error("Missing required property 'computeCapacity'");
            }
            if ((!args || args.instanceType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'instanceType'");
            }
            if ((!args || args.name === undefined) && !opts.urn) {
                throw new Error("Missing required property 'name'");
            }
            inputs["computeCapacity"] = args ? args.computeCapacity : undefined;
            inputs["description"] = args ? args.description : undefined;
            inputs["disconnectTimeoutInSeconds"] = args ? args.disconnectTimeoutInSeconds : undefined;
            inputs["displayName"] = args ? args.displayName : undefined;
            inputs["domainJoinInfo"] = args ? args.domainJoinInfo : undefined;
            inputs["enableDefaultInternetAccess"] = args ? args.enableDefaultInternetAccess : undefined;
            inputs["fleetType"] = args ? args.fleetType : undefined;
            inputs["iamRoleArn"] = args ? args.iamRoleArn : undefined;
            inputs["idleDisconnectTimeoutInSeconds"] = args ? args.idleDisconnectTimeoutInSeconds : undefined;
            inputs["imageArn"] = args ? args.imageArn : undefined;
            inputs["imageName"] = args ? args.imageName : undefined;
            inputs["instanceType"] = args ? args.instanceType : undefined;
            inputs["maxUserDurationInSeconds"] = args ? args.maxUserDurationInSeconds : undefined;
            inputs["name"] = args ? args.name : undefined;
            inputs["streamView"] = args ? args.streamView : undefined;
            inputs["tags"] = args ? args.tags : undefined;
            inputs["vpcConfig"] = args ? args.vpcConfig : undefined;
        } else {
            inputs["computeCapacity"] = undefined /*out*/;
            inputs["description"] = undefined /*out*/;
            inputs["disconnectTimeoutInSeconds"] = undefined /*out*/;
            inputs["displayName"] = undefined /*out*/;
            inputs["domainJoinInfo"] = undefined /*out*/;
            inputs["enableDefaultInternetAccess"] = undefined /*out*/;
            inputs["fleetType"] = undefined /*out*/;
            inputs["iamRoleArn"] = undefined /*out*/;
            inputs["idleDisconnectTimeoutInSeconds"] = undefined /*out*/;
            inputs["imageArn"] = undefined /*out*/;
            inputs["imageName"] = undefined /*out*/;
            inputs["instanceType"] = undefined /*out*/;
            inputs["maxUserDurationInSeconds"] = undefined /*out*/;
            inputs["name"] = undefined /*out*/;
            inputs["streamView"] = undefined /*out*/;
            inputs["tags"] = undefined /*out*/;
            inputs["vpcConfig"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(Fleet.__pulumiType, name, inputs, opts);
    }
}

/**
 * The set of arguments for constructing a Fleet resource.
 */
export interface FleetArgs {
    computeCapacity: pulumi.Input<inputs.appstream.FleetComputeCapacityArgs>;
    description?: pulumi.Input<string>;
    disconnectTimeoutInSeconds?: pulumi.Input<number>;
    displayName?: pulumi.Input<string>;
    domainJoinInfo?: pulumi.Input<inputs.appstream.FleetDomainJoinInfoArgs>;
    enableDefaultInternetAccess?: pulumi.Input<boolean>;
    fleetType?: pulumi.Input<string>;
    iamRoleArn?: pulumi.Input<string>;
    idleDisconnectTimeoutInSeconds?: pulumi.Input<number>;
    imageArn?: pulumi.Input<string>;
    imageName?: pulumi.Input<string>;
    instanceType: pulumi.Input<string>;
    maxUserDurationInSeconds?: pulumi.Input<number>;
    name: pulumi.Input<string>;
    streamView?: pulumi.Input<string>;
    tags?: pulumi.Input<pulumi.Input<inputs.appstream.FleetTagArgs>[]>;
    vpcConfig?: pulumi.Input<inputs.appstream.FleetVpcConfigArgs>;
}
