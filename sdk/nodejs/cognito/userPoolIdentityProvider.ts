// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Cognito::UserPoolIdentityProvider
 *
 * @deprecated UserPoolIdentityProvider is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
 */
export class UserPoolIdentityProvider extends pulumi.CustomResource {
    /**
     * Get an existing UserPoolIdentityProvider resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, opts?: pulumi.CustomResourceOptions): UserPoolIdentityProvider {
        pulumi.log.warn("UserPoolIdentityProvider is deprecated: UserPoolIdentityProvider is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        return new UserPoolIdentityProvider(name, undefined as any, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'aws-native:cognito:UserPoolIdentityProvider';

    /**
     * Returns true if the given object is an instance of UserPoolIdentityProvider.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is UserPoolIdentityProvider {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === UserPoolIdentityProvider.__pulumiType;
    }

    public readonly attributeMapping!: pulumi.Output<any | undefined>;
    public readonly idpIdentifiers!: pulumi.Output<string[] | undefined>;
    public readonly providerDetails!: pulumi.Output<any | undefined>;
    public readonly providerName!: pulumi.Output<string>;
    public readonly providerType!: pulumi.Output<string>;
    public readonly userPoolId!: pulumi.Output<string>;

    /**
     * Create a UserPoolIdentityProvider resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    /** @deprecated UserPoolIdentityProvider is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible. */
    constructor(name: string, args: UserPoolIdentityProviderArgs, opts?: pulumi.CustomResourceOptions) {
        pulumi.log.warn("UserPoolIdentityProvider is deprecated: UserPoolIdentityProvider is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.")
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (!opts.id) {
            if ((!args || args.providerName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'providerName'");
            }
            if ((!args || args.providerType === undefined) && !opts.urn) {
                throw new Error("Missing required property 'providerType'");
            }
            if ((!args || args.userPoolId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'userPoolId'");
            }
            resourceInputs["attributeMapping"] = args ? args.attributeMapping : undefined;
            resourceInputs["idpIdentifiers"] = args ? args.idpIdentifiers : undefined;
            resourceInputs["providerDetails"] = args ? args.providerDetails : undefined;
            resourceInputs["providerName"] = args ? args.providerName : undefined;
            resourceInputs["providerType"] = args ? args.providerType : undefined;
            resourceInputs["userPoolId"] = args ? args.userPoolId : undefined;
        } else {
            resourceInputs["attributeMapping"] = undefined /*out*/;
            resourceInputs["idpIdentifiers"] = undefined /*out*/;
            resourceInputs["providerDetails"] = undefined /*out*/;
            resourceInputs["providerName"] = undefined /*out*/;
            resourceInputs["providerType"] = undefined /*out*/;
            resourceInputs["userPoolId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        const replaceOnChanges = { replaceOnChanges: ["providerName", "providerType", "userPoolId"] };
        opts = pulumi.mergeOptions(opts, replaceOnChanges);
        super(UserPoolIdentityProvider.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * The set of arguments for constructing a UserPoolIdentityProvider resource.
 */
export interface UserPoolIdentityProviderArgs {
    attributeMapping?: any;
    idpIdentifiers?: pulumi.Input<pulumi.Input<string>[]>;
    providerDetails?: any;
    providerName: pulumi.Input<string>;
    providerType: pulumi.Input<string>;
    userPoolId: pulumi.Input<string>;
}
