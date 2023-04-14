// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ask

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

type SkillAuthenticationConfiguration struct {
	ClientId     string `pulumi:"clientId"`
	ClientSecret string `pulumi:"clientSecret"`
	RefreshToken string `pulumi:"refreshToken"`
}

// SkillAuthenticationConfigurationInput is an input type that accepts SkillAuthenticationConfigurationArgs and SkillAuthenticationConfigurationOutput values.
// You can construct a concrete instance of `SkillAuthenticationConfigurationInput` via:
//
//	SkillAuthenticationConfigurationArgs{...}
type SkillAuthenticationConfigurationInput interface {
	pulumi.Input

	ToSkillAuthenticationConfigurationOutput() SkillAuthenticationConfigurationOutput
	ToSkillAuthenticationConfigurationOutputWithContext(context.Context) SkillAuthenticationConfigurationOutput
}

type SkillAuthenticationConfigurationArgs struct {
	ClientId     pulumi.StringInput `pulumi:"clientId"`
	ClientSecret pulumi.StringInput `pulumi:"clientSecret"`
	RefreshToken pulumi.StringInput `pulumi:"refreshToken"`
}

func (SkillAuthenticationConfigurationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SkillAuthenticationConfiguration)(nil)).Elem()
}

func (i SkillAuthenticationConfigurationArgs) ToSkillAuthenticationConfigurationOutput() SkillAuthenticationConfigurationOutput {
	return i.ToSkillAuthenticationConfigurationOutputWithContext(context.Background())
}

func (i SkillAuthenticationConfigurationArgs) ToSkillAuthenticationConfigurationOutputWithContext(ctx context.Context) SkillAuthenticationConfigurationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SkillAuthenticationConfigurationOutput)
}

type SkillAuthenticationConfigurationOutput struct{ *pulumi.OutputState }

func (SkillAuthenticationConfigurationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SkillAuthenticationConfiguration)(nil)).Elem()
}

func (o SkillAuthenticationConfigurationOutput) ToSkillAuthenticationConfigurationOutput() SkillAuthenticationConfigurationOutput {
	return o
}

func (o SkillAuthenticationConfigurationOutput) ToSkillAuthenticationConfigurationOutputWithContext(ctx context.Context) SkillAuthenticationConfigurationOutput {
	return o
}

func (o SkillAuthenticationConfigurationOutput) ClientId() pulumi.StringOutput {
	return o.ApplyT(func(v SkillAuthenticationConfiguration) string { return v.ClientId }).(pulumi.StringOutput)
}

func (o SkillAuthenticationConfigurationOutput) ClientSecret() pulumi.StringOutput {
	return o.ApplyT(func(v SkillAuthenticationConfiguration) string { return v.ClientSecret }).(pulumi.StringOutput)
}

func (o SkillAuthenticationConfigurationOutput) RefreshToken() pulumi.StringOutput {
	return o.ApplyT(func(v SkillAuthenticationConfiguration) string { return v.RefreshToken }).(pulumi.StringOutput)
}

type SkillAuthenticationConfigurationPtrOutput struct{ *pulumi.OutputState }

func (SkillAuthenticationConfigurationPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SkillAuthenticationConfiguration)(nil)).Elem()
}

func (o SkillAuthenticationConfigurationPtrOutput) ToSkillAuthenticationConfigurationPtrOutput() SkillAuthenticationConfigurationPtrOutput {
	return o
}

func (o SkillAuthenticationConfigurationPtrOutput) ToSkillAuthenticationConfigurationPtrOutputWithContext(ctx context.Context) SkillAuthenticationConfigurationPtrOutput {
	return o
}

func (o SkillAuthenticationConfigurationPtrOutput) Elem() SkillAuthenticationConfigurationOutput {
	return o.ApplyT(func(v *SkillAuthenticationConfiguration) SkillAuthenticationConfiguration {
		if v != nil {
			return *v
		}
		var ret SkillAuthenticationConfiguration
		return ret
	}).(SkillAuthenticationConfigurationOutput)
}

func (o SkillAuthenticationConfigurationPtrOutput) ClientId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillAuthenticationConfiguration) *string {
		if v == nil {
			return nil
		}
		return &v.ClientId
	}).(pulumi.StringPtrOutput)
}

func (o SkillAuthenticationConfigurationPtrOutput) ClientSecret() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillAuthenticationConfiguration) *string {
		if v == nil {
			return nil
		}
		return &v.ClientSecret
	}).(pulumi.StringPtrOutput)
}

func (o SkillAuthenticationConfigurationPtrOutput) RefreshToken() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillAuthenticationConfiguration) *string {
		if v == nil {
			return nil
		}
		return &v.RefreshToken
	}).(pulumi.StringPtrOutput)
}

type SkillOverrides struct {
	Manifest interface{} `pulumi:"manifest"`
}

// SkillOverridesInput is an input type that accepts SkillOverridesArgs and SkillOverridesOutput values.
// You can construct a concrete instance of `SkillOverridesInput` via:
//
//	SkillOverridesArgs{...}
type SkillOverridesInput interface {
	pulumi.Input

	ToSkillOverridesOutput() SkillOverridesOutput
	ToSkillOverridesOutputWithContext(context.Context) SkillOverridesOutput
}

type SkillOverridesArgs struct {
	Manifest pulumi.Input `pulumi:"manifest"`
}

func (SkillOverridesArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SkillOverrides)(nil)).Elem()
}

func (i SkillOverridesArgs) ToSkillOverridesOutput() SkillOverridesOutput {
	return i.ToSkillOverridesOutputWithContext(context.Background())
}

func (i SkillOverridesArgs) ToSkillOverridesOutputWithContext(ctx context.Context) SkillOverridesOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SkillOverridesOutput)
}

func (i SkillOverridesArgs) ToSkillOverridesPtrOutput() SkillOverridesPtrOutput {
	return i.ToSkillOverridesPtrOutputWithContext(context.Background())
}

func (i SkillOverridesArgs) ToSkillOverridesPtrOutputWithContext(ctx context.Context) SkillOverridesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SkillOverridesOutput).ToSkillOverridesPtrOutputWithContext(ctx)
}

// SkillOverridesPtrInput is an input type that accepts SkillOverridesArgs, SkillOverridesPtr and SkillOverridesPtrOutput values.
// You can construct a concrete instance of `SkillOverridesPtrInput` via:
//
//	        SkillOverridesArgs{...}
//
//	or:
//
//	        nil
type SkillOverridesPtrInput interface {
	pulumi.Input

	ToSkillOverridesPtrOutput() SkillOverridesPtrOutput
	ToSkillOverridesPtrOutputWithContext(context.Context) SkillOverridesPtrOutput
}

type skillOverridesPtrType SkillOverridesArgs

func SkillOverridesPtr(v *SkillOverridesArgs) SkillOverridesPtrInput {
	return (*skillOverridesPtrType)(v)
}

func (*skillOverridesPtrType) ElementType() reflect.Type {
	return reflect.TypeOf((**SkillOverrides)(nil)).Elem()
}

func (i *skillOverridesPtrType) ToSkillOverridesPtrOutput() SkillOverridesPtrOutput {
	return i.ToSkillOverridesPtrOutputWithContext(context.Background())
}

func (i *skillOverridesPtrType) ToSkillOverridesPtrOutputWithContext(ctx context.Context) SkillOverridesPtrOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SkillOverridesPtrOutput)
}

type SkillOverridesOutput struct{ *pulumi.OutputState }

func (SkillOverridesOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SkillOverrides)(nil)).Elem()
}

func (o SkillOverridesOutput) ToSkillOverridesOutput() SkillOverridesOutput {
	return o
}

func (o SkillOverridesOutput) ToSkillOverridesOutputWithContext(ctx context.Context) SkillOverridesOutput {
	return o
}

func (o SkillOverridesOutput) ToSkillOverridesPtrOutput() SkillOverridesPtrOutput {
	return o.ToSkillOverridesPtrOutputWithContext(context.Background())
}

func (o SkillOverridesOutput) ToSkillOverridesPtrOutputWithContext(ctx context.Context) SkillOverridesPtrOutput {
	return o.ApplyTWithContext(ctx, func(_ context.Context, v SkillOverrides) *SkillOverrides {
		return &v
	}).(SkillOverridesPtrOutput)
}

func (o SkillOverridesOutput) Manifest() pulumi.AnyOutput {
	return o.ApplyT(func(v SkillOverrides) interface{} { return v.Manifest }).(pulumi.AnyOutput)
}

type SkillOverridesPtrOutput struct{ *pulumi.OutputState }

func (SkillOverridesPtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SkillOverrides)(nil)).Elem()
}

func (o SkillOverridesPtrOutput) ToSkillOverridesPtrOutput() SkillOverridesPtrOutput {
	return o
}

func (o SkillOverridesPtrOutput) ToSkillOverridesPtrOutputWithContext(ctx context.Context) SkillOverridesPtrOutput {
	return o
}

func (o SkillOverridesPtrOutput) Elem() SkillOverridesOutput {
	return o.ApplyT(func(v *SkillOverrides) SkillOverrides {
		if v != nil {
			return *v
		}
		var ret SkillOverrides
		return ret
	}).(SkillOverridesOutput)
}

func (o SkillOverridesPtrOutput) Manifest() pulumi.AnyOutput {
	return o.ApplyT(func(v *SkillOverrides) interface{} {
		if v == nil {
			return nil
		}
		return v.Manifest
	}).(pulumi.AnyOutput)
}

type SkillPackage struct {
	Overrides       *SkillOverrides `pulumi:"overrides"`
	S3Bucket        string          `pulumi:"s3Bucket"`
	S3BucketRole    *string         `pulumi:"s3BucketRole"`
	S3Key           string          `pulumi:"s3Key"`
	S3ObjectVersion *string         `pulumi:"s3ObjectVersion"`
}

// SkillPackageInput is an input type that accepts SkillPackageArgs and SkillPackageOutput values.
// You can construct a concrete instance of `SkillPackageInput` via:
//
//	SkillPackageArgs{...}
type SkillPackageInput interface {
	pulumi.Input

	ToSkillPackageOutput() SkillPackageOutput
	ToSkillPackageOutputWithContext(context.Context) SkillPackageOutput
}

type SkillPackageArgs struct {
	Overrides       SkillOverridesPtrInput `pulumi:"overrides"`
	S3Bucket        pulumi.StringInput     `pulumi:"s3Bucket"`
	S3BucketRole    pulumi.StringPtrInput  `pulumi:"s3BucketRole"`
	S3Key           pulumi.StringInput     `pulumi:"s3Key"`
	S3ObjectVersion pulumi.StringPtrInput  `pulumi:"s3ObjectVersion"`
}

func (SkillPackageArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*SkillPackage)(nil)).Elem()
}

func (i SkillPackageArgs) ToSkillPackageOutput() SkillPackageOutput {
	return i.ToSkillPackageOutputWithContext(context.Background())
}

func (i SkillPackageArgs) ToSkillPackageOutputWithContext(ctx context.Context) SkillPackageOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SkillPackageOutput)
}

type SkillPackageOutput struct{ *pulumi.OutputState }

func (SkillPackageOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SkillPackage)(nil)).Elem()
}

func (o SkillPackageOutput) ToSkillPackageOutput() SkillPackageOutput {
	return o
}

func (o SkillPackageOutput) ToSkillPackageOutputWithContext(ctx context.Context) SkillPackageOutput {
	return o
}

func (o SkillPackageOutput) Overrides() SkillOverridesPtrOutput {
	return o.ApplyT(func(v SkillPackage) *SkillOverrides { return v.Overrides }).(SkillOverridesPtrOutput)
}

func (o SkillPackageOutput) S3Bucket() pulumi.StringOutput {
	return o.ApplyT(func(v SkillPackage) string { return v.S3Bucket }).(pulumi.StringOutput)
}

func (o SkillPackageOutput) S3BucketRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SkillPackage) *string { return v.S3BucketRole }).(pulumi.StringPtrOutput)
}

func (o SkillPackageOutput) S3Key() pulumi.StringOutput {
	return o.ApplyT(func(v SkillPackage) string { return v.S3Key }).(pulumi.StringOutput)
}

func (o SkillPackageOutput) S3ObjectVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v SkillPackage) *string { return v.S3ObjectVersion }).(pulumi.StringPtrOutput)
}

type SkillPackagePtrOutput struct{ *pulumi.OutputState }

func (SkillPackagePtrOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**SkillPackage)(nil)).Elem()
}

func (o SkillPackagePtrOutput) ToSkillPackagePtrOutput() SkillPackagePtrOutput {
	return o
}

func (o SkillPackagePtrOutput) ToSkillPackagePtrOutputWithContext(ctx context.Context) SkillPackagePtrOutput {
	return o
}

func (o SkillPackagePtrOutput) Elem() SkillPackageOutput {
	return o.ApplyT(func(v *SkillPackage) SkillPackage {
		if v != nil {
			return *v
		}
		var ret SkillPackage
		return ret
	}).(SkillPackageOutput)
}

func (o SkillPackagePtrOutput) Overrides() SkillOverridesPtrOutput {
	return o.ApplyT(func(v *SkillPackage) *SkillOverrides {
		if v == nil {
			return nil
		}
		return v.Overrides
	}).(SkillOverridesPtrOutput)
}

func (o SkillPackagePtrOutput) S3Bucket() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillPackage) *string {
		if v == nil {
			return nil
		}
		return &v.S3Bucket
	}).(pulumi.StringPtrOutput)
}

func (o SkillPackagePtrOutput) S3BucketRole() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillPackage) *string {
		if v == nil {
			return nil
		}
		return v.S3BucketRole
	}).(pulumi.StringPtrOutput)
}

func (o SkillPackagePtrOutput) S3Key() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillPackage) *string {
		if v == nil {
			return nil
		}
		return &v.S3Key
	}).(pulumi.StringPtrOutput)
}

func (o SkillPackagePtrOutput) S3ObjectVersion() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *SkillPackage) *string {
		if v == nil {
			return nil
		}
		return v.S3ObjectVersion
	}).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*SkillAuthenticationConfigurationInput)(nil)).Elem(), SkillAuthenticationConfigurationArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SkillOverridesInput)(nil)).Elem(), SkillOverridesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SkillOverridesPtrInput)(nil)).Elem(), SkillOverridesArgs{})
	pulumi.RegisterInputType(reflect.TypeOf((*SkillPackageInput)(nil)).Elem(), SkillPackageArgs{})
	pulumi.RegisterOutputType(SkillAuthenticationConfigurationOutput{})
	pulumi.RegisterOutputType(SkillAuthenticationConfigurationPtrOutput{})
	pulumi.RegisterOutputType(SkillOverridesOutput{})
	pulumi.RegisterOutputType(SkillOverridesPtrOutput{})
	pulumi.RegisterOutputType(SkillPackageOutput{})
	pulumi.RegisterOutputType(SkillPackagePtrOutput{})
}
