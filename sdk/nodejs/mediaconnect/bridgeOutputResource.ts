// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource schema for AWS::MediaConnect::BridgeOutput
 */
export class BridgeOutputResource extends pulumi.CustomResource {
    /**
     * Get an existing BridgeOutputResource resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): BridgeOutputResource {
        return new BridgeOutputResource(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:mediaconnect:BridgeOutputResource';

    /**
     * Returns true if the given object is an instance of BridgeOutputResource.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is BridgeOutputResource {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === BridgeOutputResource.__pulumiType;
    }

    /**
     * The Amazon Resource Number (ARN) of the bridge.
     */
    public readonly bridgeArn!: pulumi.Output<string>;
    /**
     * The network output name.
     */
    public readonly name!: pulumi.Output<string>;
    /**
     * The output of the bridge.
     */
    public readonly networkOutput!: pulumi.Output<outputs.mediaconnect.BridgeOutputResourceBridgeNetworkOutput>;

    /**
     * Create a BridgeOutputResource resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: BridgeOutputResourceArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.bridgeArn === undefined) && !opts.urn) {
                throw new Error("Missing required property 'bridgeArn'");
            }
            if ((!args || args.networkOutput === undefined) && !opts.urn) {
                throw new Error("Missing required property 'networkOutput'");
            }
            resourceInputs["bridgeArn"] = args ? args.bridgeArn : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["networkOutput"] = args ? args.networkOutput : undefined;
        } else {
            resourceInputs["bridgeArn"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["networkOutput"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["bridgeArn", "name"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(BridgeOutputResource.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a BridgeOutputResource resource.
 */
export interface BridgeOutputResourceArgs {
    /**
     * The Amazon Resource Number (ARN) of the bridge.
     */
    bridgeArn: pulumi.Input<string>;
    /**
     * The network output name.
     */
    name?: pulumi.Input<string>;
    /**
     * The output of the bridge.
     */
    networkOutput: pulumi.Input<inputs.mediaconnect.BridgeOutputResourceBridgeNetworkOutputArgs>;
}
