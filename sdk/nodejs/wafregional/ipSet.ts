// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::WAFRegional::IPSet
 *
 * @deprecated IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class IpSet extends pulumi.CustomResource {
    /**
     * Get an existing IpSet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): IpSet {
        pulumi.log.warn("IpSet is deprecated: IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new IpSet(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:wafregional:IpSet';

    /**
     * Returns true if the given object is an instance of IpSet.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is IpSet {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === IpSet.__pulumiType;
    }

    public readonly ipSetDescriptors!: pulumi.Output<outputs.wafregional.IpSetIpSetDescriptor[] | undefined>;
    public readonly name!: pulumi.Output<string>;

    /**
     * Create a IpSet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args?: IpSetArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("IpSet is deprecated: IpSet is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            resourceInputs["ipSetDescriptors"] = args ? args.ipSetDescriptors : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
        } else {
            resourceInputs["ipSetDescriptors"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(IpSet.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a IpSet resource.
 */
export interface IpSetArgs {
    ipSetDescriptors?: pulumi.Input<pulumi.Input<inputs.wafregional.IpSetIpSetDescriptorArgs>[]>;
    name?: pulumi.Input<string>;
}
