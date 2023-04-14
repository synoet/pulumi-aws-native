// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * The AWS::VoiceID::Domain resource specifies an Amazon VoiceID Domain.
 */
export class Domain extends pulumi.CustomResource {
    /**
     * Get an existing Domain resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): Domain {
        return new Domain(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:voiceid:Domain';

    /**
     * Returns true if the given object is an instance of Domain.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is Domain {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === Domain.__pulumiType;
    }

    public readonly description!: pulumi.Output<string | undefined>;
    public /*out*/ readonly domainId!: pulumi.Output<string>;
    public readonly name!: pulumi.Output<string>;
    public readonly serverSideEncryptionConfiguration!: pulumi.Output<outputs.voiceid.DomainServerSideEncryptionConfiguration>;
    public readonly tags!: pulumi.Output<outputs.voiceid.DomainTag[] | undefined>;

    /**
     * Create a Domain resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: DomainArgs, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.serverSideEncryptionConfiguration === undefined) && !opts.urn) {
                throw new Error("Missing required property 'serverSideEncryptionConfiguration'");
            }
            resourceInputs["description"] = args ? args.description : undefined;
            resourceInputs["name"] = args ? args.name : undefined;
            resourceInputs["serverSideEncryptionConfiguration"] = args ? args.serverSideEncryptionConfiguration : undefined;
            resourceInputs["tags"] = args ? args.tags : undefined;
            resourceInputs["domainId"] = undefined /*out*/;
        } else {
            resourceInputs["description"] = undefined /*out*/;
            resourceInputs["domainId"] = undefined /*out*/;
            resourceInputs["name"] = undefined /*out*/;
            resourceInputs["serverSideEncryptionConfiguration"] = undefined /*out*/;
            resourceInputs["tags"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(Domain.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a Domain resource.
 */
export interface DomainArgs {
    description?: pulumi.Input<string>;
    name?: pulumi.Input<string>;
    serverSideEncryptionConfiguration: pulumi.Input<inputs.voiceid.DomainServerSideEncryptionConfigurationArgs>;
    tags?: pulumi.Input<pulumi.Input<inputs.voiceid.DomainTagArgs>[]>;
}
